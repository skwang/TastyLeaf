# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastyleaf_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='home',
            field=models.CharField(default=b'Empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='story',
            name='quote',
            field=models.CharField(default=b'Todo', max_length=1000),
        ),
    ]
