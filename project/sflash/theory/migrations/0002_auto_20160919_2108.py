# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theory',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]