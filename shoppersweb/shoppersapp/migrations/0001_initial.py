# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScraperItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=32)),
                ('date', models.CharField(max_length=32)),
                ('image', models.CharField(max_length=344)),
                ('link', models.CharField(max_length=324)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=322)),
                ('location', models.CharField(max_length=32)),
                ('price', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
            ],
        ),
    ]
