# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20171124_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('middle_initial', models.CharField(blank=True, max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('affiliation', models.TextField()),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.RemoveField(
            model_name='abstract',
            name='author_affiliation',
        ),
        migrations.RemoveField(
            model_name='abstract',
            name='author_name',
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='author',
            name='abstract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Abstract'),
        ),
    ]
