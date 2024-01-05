from django.contrib import admin
from .models import Post, Video, Comment, Photo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass