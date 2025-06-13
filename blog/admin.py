from django.contrib import admin
from .models import BlogCategory, BlogPost, BlogComment

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created_at')
    list_filter = ('published', 'category')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'author__username')

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at', 'approved')
    list_filter = ('approved',)
    search_fields = ('post__title', 'user__username')
