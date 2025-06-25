from django.contrib import admin
from .models import BlogPost, Comment, Like

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'timestamp')

admin.site.register(Comment)
admin.site.register(Like)
