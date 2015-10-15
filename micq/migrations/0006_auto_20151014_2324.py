# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0005_auto_20151014_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='desc',
            field=models.CharField(max_length=2000, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='token',
            field=models.CharField(max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='url',
            field=models.URLField(null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xab\x99\xe7\x82\xb9', blank=True),
        ),
    ]
