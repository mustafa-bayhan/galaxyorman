# Generated by Django 4.1.5 on 2023-01-24 02:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0034_product_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount_Product_en',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('due_date', models.DateTimeField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Productt', to='galaxy_web.product')),
            ],
        ),
    ]