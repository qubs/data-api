# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climate_data', '0009_reading_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
