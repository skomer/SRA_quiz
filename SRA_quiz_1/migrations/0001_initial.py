# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=200)),
                ('q1_answer', models.CharField(max_length=1000)),
                ('q2_answer', models.CharField(max_length=1000)),
                ('q3_answer', models.CharField(max_length=1000)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
