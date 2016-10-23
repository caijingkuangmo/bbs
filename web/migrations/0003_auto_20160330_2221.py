# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160330_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlehref',
            old_name='summary',
            new_name='title',
        ),
    ]
