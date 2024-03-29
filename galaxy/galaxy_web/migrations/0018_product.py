# Generated by Django 4.1 on 2022-12-06 10:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0017_remove_news_body_news_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/products/')),
                ('name', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('category', models.CharField(default='Nargile kömürü', max_length=100, null=True)),
            ],
        ),
    ]
