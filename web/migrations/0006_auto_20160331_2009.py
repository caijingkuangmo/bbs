# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20160330_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='summary',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='articlehref',
            old_name='title',
            new_name='summary',
        ),
    ]
