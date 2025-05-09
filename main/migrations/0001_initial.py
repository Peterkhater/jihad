# Generated by Django 5.2 on 2025-04-29 20:03

import django.db.models.deletion
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
                ('name', models.CharField(max_length=100, verbose_name='اسم الفئة')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, verbose_name='وصف الفئة')),
                ('icon', models.CharField(blank=True, help_text='اسم أيقونة Font Awesome', max_length=50)),
            ],
            options={
                'verbose_name': 'فئة المشروع',
                'verbose_name_plural': 'فئات المشاريع',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان المشروع')),
                ('description', models.TextField(verbose_name='وصف المشروع')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='صورة المشروع')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.category', verbose_name='الفئة')),
            ],
            options={
                'verbose_name': 'مشروع',
                'verbose_name_plural': 'المشاريع',
            },
        ),
    ]
