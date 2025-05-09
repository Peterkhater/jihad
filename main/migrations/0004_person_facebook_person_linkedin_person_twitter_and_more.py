# Generated by Django 5.2 on 2025-04-30 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_familymember_options_familymember_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='vision',
            field=models.TextField(blank=True, verbose_name='الرؤية'),
        ),
        migrations.CreateModel(
            name='EducationalQualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='المؤهل العلمي')),
                ('institution', models.CharField(max_length=200, verbose_name='المؤسسة التعليمية')),
                ('year', models.PositiveIntegerField(verbose_name='سنة الحصول')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qualifications', to='main.person', verbose_name='المرشح')),
            ],
            options={
                'verbose_name': 'المؤهل العلمي',
                'verbose_name_plural': 'المؤهلات العلمية',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='الهدف')),
                ('description', models.TextField(verbose_name='تفاصيل الهدف')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='main.person', verbose_name='المرشح')),
            ],
            options={
                'verbose_name': 'الهدف',
                'verbose_name_plural': 'الأهداف',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200, verbose_name='المنصب')),
                ('organization', models.CharField(max_length=200, verbose_name='المؤسسة')),
                ('start_year', models.PositiveIntegerField(verbose_name='سنة البدء')),
                ('end_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='سنة الانتهاء')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='main.person', verbose_name='المرشح')),
            ],
            options={
                'verbose_name': 'الخبرة العملية',
                'verbose_name_plural': 'الخبرات العملية',
            },
        ),
    ]
