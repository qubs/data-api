# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 15:27
from __future__ import unicode_literals

from django.db import migrations

from datetime import timedelta


# noinspection PyUnusedLocal
def add_message_id_to_reading(apps, schema_editor):
    # noinspection PyPep8Naming
    Reading = apps.get_model('climate_data', 'Reading')
    # noinspection PyPep8Naming
    Message = apps.get_model('climate_data', 'Message')

    for reading in Reading.objects.filter(message_id=None):
        reading.message = Message.objects.filter(
            station=reading.station,
            arrival_time__gt=reading.read_time,
            arrival_time__lt=(reading.read_time + timedelta(minutes=52))
        ).first()
        reading.save()


class Migration(migrations.Migration):

    dependencies = [
        ('climate_data', '0028_auto_20170627_1914'),
    ]

    operations = [
        migrations.RunPython(add_message_id_to_reading),
    ]