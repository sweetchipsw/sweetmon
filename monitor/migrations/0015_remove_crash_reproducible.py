# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_auto_20170713_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crash',
            name='reproducible',
        ),
    ]
