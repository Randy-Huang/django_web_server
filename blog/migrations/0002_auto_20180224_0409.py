# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-23 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Unique ID'),
        ),
    ]
