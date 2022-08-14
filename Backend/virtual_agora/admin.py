from django.contrib import admin
from virtual_agora.models import Theme, Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'status', 'slug',
                    'author', 'published_date')
    # prepopulated_fields: {'slug': ('title',), }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'body',
                    'post', 'parent', 'created')


admin.site.register(Theme)
