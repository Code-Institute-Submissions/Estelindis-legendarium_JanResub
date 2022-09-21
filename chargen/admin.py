from django.contrib import admin
from .models import Story
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    summernote_fields = ('story')
