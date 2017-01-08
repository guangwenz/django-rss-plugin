# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssplugin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssplugin',
            name='template',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
