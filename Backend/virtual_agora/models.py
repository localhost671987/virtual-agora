from pyexpat import model
from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    post_types = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    theme = models.ManyToManyField(Theme, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published_date')
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(
        max_length=15, choices=post_types, default='published')
    objects = models.Manager()  # default manager
    post_objects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published_date',
                    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

    def children(self):
        return Comment.objects.filter(parent=self)



