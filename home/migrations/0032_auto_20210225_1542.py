# Generated by Django 3.1.5 on 2021-02-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20210225_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_images',
            name='Refrence_image',
            field=models.ImageField(default='category/media/default.jpg', upload_to='category/media/'),
        ),
        migrations.AlterField(
            model_name='category_images',
            name='category_type',
            field=models.IntegerField(choices=[[0, 'Default'], [1, 'Dyes & Intermidiates'], [2, 'Food & Pharma'], [3, 'Varieties in Cosmetic'], [4, 'Shades of  pigments'], [5, 'Intermediates'], [6, 'Acid Dyes'], [7, 'Basic Dyes'], [8, 'Direct Dyes'], [9, 'Food & Lake Color'], [10, 'Solvet Dyes'], [11, 'Reactive Dyes']], default=0),
        ),
    ]
