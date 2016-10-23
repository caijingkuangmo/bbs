# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlehref',
            name='img',
            field=models.ImageField(null=True, upload_to=b'uploads', blank=True),
        ),
        migrations.AlterField(
            model_name='articlepicture',
            name='img',
            field=models.ImageField(upload_to=b'uploads'),
        ),
    ]
