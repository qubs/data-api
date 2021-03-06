# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 02:41
from __future__ import unicode_literals

from django.db import migrations, models
import herbarium_data.models


class Migration(migrations.Migration):

    dependencies = [
        ('herbarium_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specimen',
            name='date_collected',
        ),
        migrations.AddField(
            model_name='specimen',
            name='day_collected',
            field=models.PositiveSmallIntegerField(null=True, validators=[herbarium_data.models.validate_day_of_month]),
        ),
        migrations.AddField(
            model_name='specimen',
            name='month_collected',
            field=models.PositiveSmallIntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
        migrations.AddField(
            model_name='specimen',
            name='year_collected',
            field=models.PositiveSmallIntegerField(null=True, validators=[herbarium_data.models.validate_year]),
        ),
    ]
