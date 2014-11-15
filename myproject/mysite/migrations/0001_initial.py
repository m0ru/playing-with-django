# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('street', models.CharField(max_length=200)),
                ('houseNr', models.IntegerField()),
                ('city', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('address', models.ForeignKey(to='mysite.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
