# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastyleaf_app', '0002_auto_20151202_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.CharField(default=b'Anonymous', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='home',
            field=models.CharField(default=b'Nothing', max_length=100, blank=True),
        ),
    ]
