# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-13 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200302_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
