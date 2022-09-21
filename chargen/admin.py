from django.contrib import admin
from .models import Category, Story, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('name', 'summary')}
    summernote_fields = ('story', 'notes')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['category_name']}
    list_filter = ['category_name']
    list_display = ('category_name', 'category_pic', 'slug')
