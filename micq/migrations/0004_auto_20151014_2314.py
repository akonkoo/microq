# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0003_myuser_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='desc',
            field=models.CharField(max_length=2000, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', db_index=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.CharField(default=b'M', max_length=50, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='url',
            field=models.URLField(null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xab\x99\xe7\x82\xb9'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', db_index=True),
        ),
    ]
