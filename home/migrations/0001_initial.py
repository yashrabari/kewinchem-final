# Generated by Django 3.1.5 on 2021-01-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='intermediates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('case_no', models.CharField(max_length=100)),
            ],
        ),
    ]
