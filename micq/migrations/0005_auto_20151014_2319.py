# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0004_auto_20151014_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
