# Generated by Django 5.2 on 2025-04-30 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_person_facebook_person_linkedin_person_twitter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='family_members',
        ),
        migrations.AddField(
            model_name='familymember',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='famMember', to='main.person', verbose_name='المرشح'),
        ),
    ]
