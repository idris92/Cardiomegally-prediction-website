# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-06-12 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naccounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='prediction',
            field=models.CharField(default='Negative', max_length=200),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='report',
            field=models.TextField(max_length=500),
        ),
    ]
