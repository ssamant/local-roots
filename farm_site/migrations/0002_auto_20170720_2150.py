# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-21 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(default=124, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.CharField(default=456, max_length=25),
            preserve_default=False,
        ),
    ]