# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('codigo_postal', models.IntegerField()),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('actualizado', models.DateField(auto_now=True)),
            ],
        ),
    ]
