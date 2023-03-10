from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tag')
    list_display = ('title', 'date', 'author')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'date')
    list_filter = ('date', 'post')


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)