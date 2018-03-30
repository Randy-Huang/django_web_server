# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 16:53
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Title')),
                ('unique_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Unique ID')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Content')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_time', models.DateTimeField(blank=True, null=True)),
                ('modified_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
