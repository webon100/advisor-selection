# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 02:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0010_auto_20160505_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='advisor',
        ),
        migrations.RemoveField(
            model_name='student',
            name='uid',
        ),
        migrations.AlterField(
            model_name='advisor',
            name='photo',
            field=models.ImageField(upload_to='faces'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='selection',
            name='advisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Advisor'),
        ),
        migrations.AddField(
            model_name='selection',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
