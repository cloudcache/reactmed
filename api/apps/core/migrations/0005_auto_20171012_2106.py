# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 21:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171011_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'ADMIN'), ('DOCTOR', 'DOCTOR')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 21, 6, 38, 526856, tzinfo=utc)),
        ),
    ]
