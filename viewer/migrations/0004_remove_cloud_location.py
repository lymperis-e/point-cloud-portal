# Generated by Django 4.0 on 2022-01-12 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_cloud_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cloud',
            name='location',
        ),
    ]
