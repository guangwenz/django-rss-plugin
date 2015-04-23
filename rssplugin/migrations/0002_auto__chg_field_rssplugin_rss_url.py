# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from rssplugin.utils import rename_tables_new_to_old


class Migration(SchemaMigration):

    def forwards(self, orm):
        rename_tables_new_to_old(db)

        # Changing field 'RSSPlugin.rss_url'
        db.alter_column('cmsplugin_rssplugin', 'rss_url', self.gf('django.db.models.fields.CharField')(max_length=512))

    def backwards(self, orm):
        rename_tables_new_to_old(db)

        # Changing field 'RSSPlugin.rss_url'
        db.alter_column('cmsplugin_rssplugin', 'rss_url', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 12, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'rssplugin.rssplugin': {
            'Meta': {'object_name': 'RSSPlugin', 'db_table': "'cmsplugin_rssplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cache_time': ('django.db.models.fields.IntegerField', [], {}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '6'}),
            'open_in_new_window': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rss_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Community News'", 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['rssplugin']