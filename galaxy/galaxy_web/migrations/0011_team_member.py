# Generated by Django 3.2.15 on 2022-12-06 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy_web', '0010_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Member Name')),
                ('position', models.CharField(max_length=100, null=True, verbose_name='Member Position')),
                ('facebook_link', models.CharField(blank=True, max_length=150, null=True)),
                ('instangram_link', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
