from django.contrib import admin
from .models import Category, Story, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'summary', 'story', 'notes']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('name', 'summary')}
    summernote_fields = ('story', 'notes')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['category_name']}
    list_filter = ['category_name']
    list_display = ('category_name', 'category_pic', 'slug')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'story', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
