# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-07 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0053_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='native_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
