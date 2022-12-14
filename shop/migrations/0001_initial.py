# Generated by Django 4.1 on 2022-08-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='prace')),
            ],
            options={
                'verbose_name': 'prace',
                'verbose_name_plural': 'prace',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='product')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
            },
        ),
    ]
