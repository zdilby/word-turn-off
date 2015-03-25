# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Words'
        db.create_table(u'game_words', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('classify', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('features', self.gf('django.db.models.fields.TextField')(max_length=256)),
        ))
        db.send_create_signal(u'game', ['Words'])

        # Adding model 'WordsSet'
        db.create_table(u'game_wordsset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pernum', self.gf('django.db.models.fields.IntegerField')()),
            ('orderby', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'game', ['WordsSet'])


    def backwards(self, orm):
        # Deleting model 'Words'
        db.delete_table(u'game_words')

        # Deleting model 'WordsSet'
        db.delete_table(u'game_wordsset')


    models = {
        u'game.words': {
            'Meta': {'object_name': 'Words'},
            'classify': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'game.wordsset': {
            'Meta': {'object_name': 'WordsSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orderby': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'pernum': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['game']