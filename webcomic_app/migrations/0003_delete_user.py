# Generated by Django 4.2.5 on 2023-10-19 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcomic_app', '0002_series_chapter_series'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
