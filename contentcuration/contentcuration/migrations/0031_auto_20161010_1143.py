# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 18:43
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0030_auto_20161005_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentitem',
            name='raw_data',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='formatpreset',
            name='id',
            field=models.CharField(choices=[('high_res_video', 'High Resolution'), ('low_res_video', 'Low Resolution'), ('vector_video', 'Vectorized'), ('video_thumbnail', 'Thumbnail'), ('video_subtitle', 'Subtitle'), ('audio', 'Audio'), (
                'audio_thumbnail', 'Thumbnail'), ('document', 'Document'), ('document_thumbnail', 'Thumbnail'), ('exercise', 'Exercise'), ('exercise_thumbnail', 'Thumbnail')], max_length=150, primary_key=True, serialize=False),
        ),
    ]
