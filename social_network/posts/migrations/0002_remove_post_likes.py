# Generated by Django 5.0.2 on 2024-06-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
