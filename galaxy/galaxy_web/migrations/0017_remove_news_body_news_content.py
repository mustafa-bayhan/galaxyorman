# Generated by Django 4.1 on 2022-12-06 09:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0016_alter_news_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
