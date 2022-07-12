from django.contrib import admin
from virtual_agora.models import Theme, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'status', 'slug', 'author', 'published_date')
    # prepopulated_fields: {'slug': ('title',), }


admin.site.register(Theme)
