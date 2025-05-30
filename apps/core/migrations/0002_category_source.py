# Generated by Django 5.2.1 on 2025-05-21 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='category name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='source name')),
            ],
            options={
                'verbose_name': 'source',
                'verbose_name_plural': 'sources',
            },
        ),
    ]
