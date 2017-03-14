# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
