from django.contrib import admin
from .models import Post, Comment, PostImage, Like


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class LikeInline(admin.TabularInline):
    model = Like
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, CommentInline, LikeInline]
    list_display = ('author', 'text', 'create_at', 'id')
    search_fields = ('text', 'author__username')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_at', 'post')
    list_filter = ('post',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('post',)
