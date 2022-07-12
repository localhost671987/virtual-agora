from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
        User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(
        max_length=15, choices=post_types, default='published')
    objects = models.Manager()  # default manager
    post_objects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published_date',
                    )

    def __str__(self):
        return self.title
