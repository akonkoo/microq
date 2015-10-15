# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', db_index=True)),
                ('username', models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', db_index=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('sex', models.CharField(max_length=50, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'M', b'\xe7\x94\xb7'), (b'F', b'\xe5\xa5\xb3')])),
                ('url', models.URLField(null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xab\x99\xe7\x82\xb9')),
                ('desc', models.CharField(max_length=2000, null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\xae\x80\xe4\xbb\x8b')),
                ('avatar', models.CharField(max_length=500, null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
                ('token', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
