# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20160504_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='photo',
            field=models.ImageField(upload_to='faces'),
        ),
    ]