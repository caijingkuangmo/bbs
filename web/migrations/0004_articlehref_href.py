# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160330_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlehref',
            name='href',
            field=models.CharField(default=b'http://www.cnblogs.com/Eva_J', max_length=255),
        ),
    ]
