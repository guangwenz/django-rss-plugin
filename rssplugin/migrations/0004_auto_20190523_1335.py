# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssplugin', '0003_auto_20161210_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
