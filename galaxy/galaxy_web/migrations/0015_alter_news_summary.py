# Generated by Django 4.1 on 2022-12-06 09:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0014_news_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]