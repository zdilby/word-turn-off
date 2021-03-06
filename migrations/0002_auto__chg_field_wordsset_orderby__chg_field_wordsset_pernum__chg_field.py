# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WordsSet.orderby'
        db.alter_column(u'game_wordsset', 'orderby', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'WordsSet.pernum'
        db.alter_column(u'game_wordsset', 'pernum', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Words.level'
        db.alter_column(u'game_words', 'level', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Words.features'
        db.alter_column(u'game_words', 'features', self.gf('django.db.models.fields.TextField')(max_length=256, null=True))

    def backwards(self, orm):

        # Changing field 'WordsSet.orderby'
        db.alter_column(u'game_wordsset', 'orderby', self.gf('django.db.models.fields.CharField')(default=None, max_length=64))

        # Changing field 'WordsSet.pernum'
        db.alter_column(u'game_wordsset', 'pernum', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Words.level'
        db.alter_column(u'game_words', 'level', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Words.features'
        db.alter_column(u'game_words', 'features', self.gf('django.db.models.fields.TextField')(default=None, max_length=256))

    models = {
        u'game.words': {
            'Meta': {'object_name': 'Words'},
            'classify': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'game.wordsset': {
            'Meta': {'object_name': 'WordsSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orderby': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'pernum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game']