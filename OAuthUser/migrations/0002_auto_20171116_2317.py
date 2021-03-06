# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OAuthUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuserextra',
            options={'verbose_name': '认证用户附加信息', 'verbose_name_plural': '认证用户附加信息'},
        ),
        migrations.AlterField(
            model_name='tuserextra',
            name='local_privileges',
            field=models.TextField(help_text='本地记录的权限列表', null=True, verbose_name='本地记录的权限列表'),
        ),
        migrations.AlterField(
            model_name='tuserextra',
            name='remote_privileges',
            field=models.TextField(help_text='认证服务器返回的权限列表', null=True, verbose_name='认证服务器返回的权限列表'),
        ),
    ]
