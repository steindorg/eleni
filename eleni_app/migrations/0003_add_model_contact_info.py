# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact_info'
        db.create_table('eleni_app_contact_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(blank=True, max_length=60)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, max_length=60)),
            ('additional_1', self.gf('django.db.models.fields.CharField')(blank=True, max_length=60)),
            ('additional_2', self.gf('django.db.models.fields.CharField')(blank=True, max_length=60)),
        ))
        db.send_create_signal('eleni_app', ['Contact_info'])


    def backwards(self, orm):
        # Deleting model 'Contact_info'
        db.delete_table('eleni_app_contact_info')


    models = {
        'eleni_app.about_detail': {
            'Meta': {'object_name': 'About_detail'},
            'description_box1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'eleni_app.contact_info': {
            'Meta': {'object_name': 'Contact_info'},
            'additional_1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'additional_2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'email': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'})
        },
        'eleni_app.link': {
            'Meta': {'object_name': 'Link'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'eleni_app.photo': {
            'Meta': {'object_name': 'Photo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'eleni_app.project': {
            'Meta': {'object_name': 'Project'},
            'description_box1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_box2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['eleni_app.Photo']", 'symmetrical': 'False'}),
            'preview_date': ('django.db.models.fields.DateField', [], {}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'role1': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role2': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role3': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role4': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role5': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role6': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role7': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role8': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'role9': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'to': "orm['eleni_app.Video_Link']"})
        },
        'eleni_app.video_link': {
            'Meta': {'object_name': 'Video_Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'video': ('embed_video.fields.EmbedVideoField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['eleni_app']