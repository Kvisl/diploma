# Generated by Django 5.0.2 on 2024-07-01 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_userpostrelation_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpostrelation',
            old_name='text',
            new_name='comment',
        ),
    ]