# Generated by Django 4.1 on 2023-01-08 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0023_remove_discount_product_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount_product',
            name='duration',
        ),
        migrations.AddField(
            model_name='discount_product',
            name='day',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='discount_product',
            name='hour',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AddField(
            model_name='discount_product',
            name='minute',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)]),
        ),
    ]