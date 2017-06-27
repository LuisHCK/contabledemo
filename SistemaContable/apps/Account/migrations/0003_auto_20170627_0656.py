# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20170627_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.AccountCategory'),
        ),
    ]
