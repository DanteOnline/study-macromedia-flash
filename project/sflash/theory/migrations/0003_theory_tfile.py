# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0002_auto_20160919_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='theory',
            name='tfile',
            field=models.FileField(blank=True, null=True, upload_to='tfiles'),
        ),
    ]
