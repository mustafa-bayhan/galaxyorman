# Generated by Django 4.1 on 2022-12-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0019_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Yayınlanma Tarihi'),
        ),
    ]
