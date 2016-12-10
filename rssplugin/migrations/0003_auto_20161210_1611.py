# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssplugin', '0002_rssplugin_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(to='cms.CMSPlugin', related_name='rssplugin_rssplugin', parent_link=True, serialize=False, primary_key=True, auto_created=True),
        ),
        migrations.AlterField(
            model_name='rssplugin',
            name='count',
            field=models.IntegerField(verbose_name='Number of Entries', default=6),
        ),
        migrations.AlterField(
            model_name='rssplugin',
            name='template',
            field=models.CharField(default='', blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='rssplugin',
            name='title',
            field=models.CharField(max_length=200, default='Community News', help_text="If you specify this value, it will replace feed's title", blank=True, null=True),
        ),
    ]
