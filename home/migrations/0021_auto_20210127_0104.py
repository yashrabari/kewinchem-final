# Generated by Django 3.1.5 on 2021-01-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_lake_color_dyes_other_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lake_color_dyes',
            name='CI_refrence',
        ),
        migrations.RemoveField(
            model_name='lake_color_dyes',
            name='FD_C_color',
        ),
        migrations.AlterField(
            model_name='lake_color_dyes',
            name='ci_no',
            field=models.CharField(max_length=100),
        ),
    ]
