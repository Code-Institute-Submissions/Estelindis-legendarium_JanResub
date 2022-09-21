# Generated by Django 3.2.14 on 2022-09-21 13:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chargen', '0003_update_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='Story',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='character',
            new_name='story',
        ),
    ]
