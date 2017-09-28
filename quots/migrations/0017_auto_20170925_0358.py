# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quots', '0016_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apicall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(default='null', max_length=4, verbose_name='사용자명')),
                ('name', models.CharField(default='null', max_length=30, verbose_name='아이디')),
                ('type', models.CharField(max_length=200, verbose_name='검색용도')),
                ('content', models.CharField(max_length=200, verbose_name='검색내용')),
                ('update', models.DateTimeField(default=django.utils.timezone.now, verbose_name='사용일시')),
            ],
        ),
        migrations.RemoveField(
            model_name='in',
            name='answered',
        ),
        migrations.RemoveField(
            model_name='in',
            name='orderer',
        ),
        migrations.DeleteModel(
            name='ordering',
        ),
        migrations.RemoveField(
            model_name='out',
            name='handler',
        ),
        migrations.RemoveField(
            model_name='out',
            name='parent',
        ),
        migrations.DeleteModel(
            name='In',
        ),
        migrations.DeleteModel(
            name='Inner',
        ),
        migrations.DeleteModel(
            name='Out',
        ),
        migrations.DeleteModel(
            name='Outer',
        ),
    ]
