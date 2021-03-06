# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('task_details', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished_date', models.DateTimeField(blank=True, null=True)),
                ('project_field', models.CharField(max_length=255)),
            ],
        ),
    ]
