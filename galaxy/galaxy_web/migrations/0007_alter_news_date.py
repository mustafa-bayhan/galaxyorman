# Generated by Django 4.1 on 2022-12-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0006_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.CharField(default='Aralık 2022', max_length=200),
        ),
    ]