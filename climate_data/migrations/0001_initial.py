# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('read_time', models.DateTimeField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('data_id', models.CharField(max_length=20)),
                ('decimals', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('goes_id', models.CharField(max_length=8)),
                ('sensors', models.ManyToManyField(to='climate_data.Sensor')),
            ],
        ),
        migrations.AddField(
            model_name='reading',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='climate_data.Sensor'),
        ),
        migrations.AddField(
            model_name='reading',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='climate_data.Station'),
        ),
    ]
