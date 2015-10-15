# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='sex',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='desc',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'Email', db_index=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(unique=True, max_length=50, db_index=True),
        ),
    ]
