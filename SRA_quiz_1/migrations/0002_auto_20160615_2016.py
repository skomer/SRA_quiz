# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRA_quiz_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onemodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
