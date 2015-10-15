# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0002_auto_20151014_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default=b'M', max_length=50, choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
        ),
    ]
