# Generated by Django 3.1.5 on 2021-01-26 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210127_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lake_color_dyes',
            old_name='EC_no',
            new_name='EEC_no',
        ),
    ]