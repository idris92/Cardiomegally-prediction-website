# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-06-15 01:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naccounts', '0007_auto_20190615_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='date',
        ),
    ]