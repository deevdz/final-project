from django.contrib import admin
from .models import Category, Blog, Comment

# Admin - Category: What to display and prepopulate the slug field with the category title
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'blurb')
    prepopulated_fields = {'slug': ('title',)}

# Admin - Blog Posts: What to display and prepopulate the slug field with the category title, show a filter with the criteria specified and fields that can be searched
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'status', 'featured')
    list_filter = ('published', 'featured')
    search_fields = ('title', 'content', 'tag')
    prepopulated_fields = {'slug': ('title',)}

# Admin - Comments: What to display in the list view of comments
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'blog', 'timestamp', 'approved')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
