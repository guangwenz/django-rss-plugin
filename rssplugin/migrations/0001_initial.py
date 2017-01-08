# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('count', models.IntegerField(default=6)),
                ('title', models.CharField(default=b'Community News', max_length=200, null=True, help_text="If you specified this value, it will replace feed's title")),
                ('rss_url', models.CharField(max_length=512)),
                ('open_in_new_window', models.BooleanField(default=False)),
                ('cache_time', models.IntegerField(verbose_name='Cache time in seconds')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
