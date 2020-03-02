# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-02 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='index_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('images', models.ImageField(blank=True, null=True, upload_to='img')),
                ('imagess', models.ImageField(blank=True, null=True, upload_to='img')),
                ('imagesss', models.ImageField(blank=True, null=True, upload_to='img')),
                ('imagessss', models.ImageField(blank=True, null=True, upload_to='img')),
                ('imagesssss', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]