# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0008_auto_20151015_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='created_by',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default=b'M', max_length=5, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
        ),
    ]
