# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-05-18 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdepartment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mdepartment',
            new_name='Mdepartments',
        ),
    ]