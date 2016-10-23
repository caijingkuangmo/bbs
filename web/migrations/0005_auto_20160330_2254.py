# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_articlehref_href'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlehref',
            old_name='href',
            new_name='articlehref',
        ),
    ]
