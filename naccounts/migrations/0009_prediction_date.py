# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-06-15 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naccounts', '0008_remove_prediction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
