# Generated by Django 3.2.14 on 2022-09-21 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chargen', '0005_rename_story_props'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Stories'},
        ),
    ]
