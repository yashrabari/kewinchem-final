# Generated by Django 3.1.5 on 2021-01-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_news_feed_post_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_images',
            name='image',
            field=models.ImageField(upload_to='news_feed'),
        ),
    ]
