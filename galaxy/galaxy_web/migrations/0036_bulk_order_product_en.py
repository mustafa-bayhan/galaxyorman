# Generated by Django 4.1.5 on 2023-01-24 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0035_discount_product_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bulk_Order_Product_en',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='The_Productt', to='galaxy_web.product_en')),
            ],
        ),
    ]
