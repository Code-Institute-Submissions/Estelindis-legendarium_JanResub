from django.contrib import admin
from .models import Character
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Character)
class CharAdmin(SummernoteModelAdmin):

    summernote_fields = ('story')
