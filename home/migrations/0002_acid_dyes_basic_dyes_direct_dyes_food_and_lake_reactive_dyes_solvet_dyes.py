# Generated by Django 3.1.5 on 2021-01-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='acid_dyes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI_Name', models.CharField(max_length=200)),
                ('Case_no', models.CharField(max_length=100)),
                ('Application', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='basic_dyes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('case_no', models.CharField(max_length=100)),
                ('compound', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='direct_dyes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI_Name', models.CharField(max_length=100)),
                ('case_no', models.CharField(max_length=100)),
                ('Application', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='food_and_lake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('ci_no', models.IntegerField()),
                ('FD_C_color', models.CharField(max_length=100)),
                ('CI_refrence', models.CharField(max_length=100)),
                ('EC_no', models.CharField(max_length=100)),
                ('case_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='reactive_dyes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('case_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='solvet_dyes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('case_no', models.CharField(max_length=100)),
            ],
        ),
    ]