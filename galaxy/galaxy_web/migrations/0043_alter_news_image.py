# Generated by Django 4.1.5 on 2023-01-25 19:10

from django.db import migrations, models
import galaxy_web.models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0042_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='image/', validators=[galaxy_web.models.file_size]),
        ),
    ]
