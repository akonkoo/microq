# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0009_auto_20151015_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='question',
            name='comments',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', blank=True, to='micq.Question', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(verbose_name=b'\xe7\xad\x94\xe6\xa1\x88', blank=True, to='micq.Answer', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98', blank=True, to='micq.Question', null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
    ]
