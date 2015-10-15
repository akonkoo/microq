# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('micq', '0007_auto_20151014_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['-created'], 'verbose_name': '\u7b54\u6848', 'verbose_name_plural': '\u7b54\u6848'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created'], 'verbose_name': '\u95ee\u9898', 'verbose_name_plural': '\u95ee\u9898'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6807\u7b7e', 'verbose_name_plural': '\u6807\u7b7e'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(verbose_name=b'\xe7\xad\x94\xe6\xa1\x88\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='comments',
            field=models.ManyToManyField(to='micq.Comment', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='count',
            field=models.IntegerField(default=0, null=True, verbose_name=b'\xe8\xae\xa1\xe6\x95\xb0'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_by',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='micq.Answer', verbose_name=b'\xe7\xad\x94\xe6\xa1\x88'),
        ),
        migrations.AlterField(
            model_name='question',
            name='body',
            field=models.TextField(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='question',
            name='comments',
            field=models.ManyToManyField(to='micq.Comment', verbose_name=b'\xe8\xaf\x84\xe8\xae\xba'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='micq.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=150, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
