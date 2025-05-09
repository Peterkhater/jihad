# Generated by Django 5.2 on 2025-04-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='الاسم')),
                ('last_name', models.CharField(max_length=200, verbose_name='الشهرة')),
                ('age', models.PositiveIntegerField(verbose_name='العمر')),
                ('relation', models.CharField(max_length=200, verbose_name='صلة القرابة')),
                ('occupation', models.CharField(blank=True, max_length=200, verbose_name='المهنة')),
            ],
            options={
                'verbose_name': 'عضو الأسرة',
                'verbose_name_plural': 'أعضاء الأسرة',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='اسم المرشح')),
                ('last_name', models.CharField(max_length=200, verbose_name='شهرة المرشح')),
                ('position', models.CharField(max_length=100, verbose_name='المنصب')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='صورة المرشح')),
                ('age', models.PositiveIntegerField(verbose_name='العمر')),
                ('note', models.TextField(blank=True, verbose_name='ملاحظات')),
                ('election_program', models.TextField(blank=True, verbose_name='البرنامج الانتخابي')),
                ('is_current_candidate', models.BooleanField(default=True, verbose_name='مرشح حاليا')),
                ('family_members', models.ManyToManyField(blank=True, to='main.familymember', verbose_name='أفراد الأسرة')),
            ],
            options={
                'verbose_name': 'مرشح',
                'verbose_name_plural': 'المرشحين',
                'ordering': ['position', 'last_name'],
            },
        ),
    ]
