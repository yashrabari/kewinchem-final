# Generated by Django 3.1.5 on 2021-01-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_flouroscent_pigments_shades_and_pigment'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('our_vision', models.TextField()),
                ('out_mission', models.TextField()),
                ('our_value', models.TextField()),
            ],
        ),
    ]
