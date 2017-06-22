# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbarium_data', '0002_auto_20170613_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='country',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='collectors',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='county',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='habitat',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='location',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='specimen',
            name='township',
            field=models.CharField(default='', max_length=127),
        ),
    ]