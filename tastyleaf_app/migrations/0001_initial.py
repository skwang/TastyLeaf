# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(default=b'Anonymous', max_length=100)),
                ('fullstory', models.CharField(max_length=1000)),
                ('quote', models.CharField(max_length=1000)),
                ('question', models.CharField(max_length=200)),
                ('home', models.CharField(max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('imgurl', models.CharField(max_length=300)),
            ],
        ),
    ]
