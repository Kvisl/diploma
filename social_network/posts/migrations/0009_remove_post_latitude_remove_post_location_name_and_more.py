# Generated by Django 5.0.2 on 2024-07-09 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_latitude_post_location_name_post_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='post',
            name='location_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='longitude',
        ),
    ]