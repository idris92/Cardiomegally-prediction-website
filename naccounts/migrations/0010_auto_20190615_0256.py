# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-06-15 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naccounts', '0009_prediction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]