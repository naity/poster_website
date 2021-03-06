# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='abstract',
        ),
        migrations.AddField(
            model_name='abstract',
            name='author_affiliation',
            field=models.CharField(default='a', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abstract',
            name='author_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
