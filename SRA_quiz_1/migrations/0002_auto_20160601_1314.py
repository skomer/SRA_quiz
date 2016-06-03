# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRA_quiz_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='q1_answer',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='q2_answer',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='q3_answer',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
