# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0010_auto_20151019_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='desc',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default=b'M', max_length=5, choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(unique=True, max_length=50, db_index=True),
        ),
    ]
