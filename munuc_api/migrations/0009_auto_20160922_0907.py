# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('munuc_api', '0008_auto_20160922_0855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BaseUser',
            new_name='ExtendedUser',
        ),
    ]