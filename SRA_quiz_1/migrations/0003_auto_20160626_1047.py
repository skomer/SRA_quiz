# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRA_quiz_1', '0002_auto_20160615_2016'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Onemodel',
            new_name='Entry',
        ),
    ]
