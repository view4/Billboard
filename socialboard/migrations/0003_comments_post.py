# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-31 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialboard', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='socialboard.Post'),
        ),
    ]
