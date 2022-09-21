from django.contrib import admin
from .models import Category, Story, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    summernote_fields = ('story')
