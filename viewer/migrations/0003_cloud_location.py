# Generated by Django 4.0 on 2022-01-12 17:23

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_remove_cloud_box_remove_cloud_lat_remove_cloud_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloud',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default='POINT(40.6254868487 22.9296330649)', srid=4326),
        ),
    ]
