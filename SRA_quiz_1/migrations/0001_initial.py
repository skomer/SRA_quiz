# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onemodel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('status', models.BooleanField()),
                ('q1_answer', models.CharField(max_length=1000, null=True)),
                ('q2_answer', models.CharField(max_length=1000, null=True)),
                ('q3_answer', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
