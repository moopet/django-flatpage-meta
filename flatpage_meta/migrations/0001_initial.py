# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MetaTagType'
        db.create_table('flatpage_meta_metatagtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('format_string', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('allow_multiple', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('flatpage_meta', ['MetaTagType'])

        # Adding model 'FlatPageMetaTag'
        db.create_table('flatpage_meta_flatpagemetatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_tag_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flatpage_meta_flatpagemetatag_related', to=orm['flatpage_meta.MetaTagType'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meta_tag_set', to=orm['flatpages.FlatPage'])),
        ))
        db.send_create_signal('flatpage_meta', ['FlatPageMetaTag'])

        # Adding model 'SiteMetaTag'
        db.create_table('flatpage_meta_sitemetatag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_tag_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='flatpage_meta_sitemetatag_related', to=orm['flatpage_meta.MetaTagType'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meta_tag_set', to=orm['sites.Site'])),
        ))
        db.send_create_signal('flatpage_meta', ['SiteMetaTag'])


    def backwards(self, orm):
        # Deleting model 'MetaTagType'
        db.delete_table('flatpage_meta_metatagtype')

        # Deleting model 'FlatPageMetaTag'
        db.delete_table('flatpage_meta_flatpagemetatag')

        # Deleting model 'SiteMetaTag'
        db.delete_table('flatpage_meta_sitemetatag')


    models = {
        'flatpage_meta.flatpagemetatag': {
            'Meta': {'object_name': 'FlatPageMetaTag'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meta_tag_set'", 'to': "orm['flatpages.FlatPage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_tag_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flatpage_meta_flatpagemetatag_related'", 'to': "orm['flatpage_meta.MetaTagType']"})
        },
        'flatpage_meta.metatagtype': {
            'Meta': {'object_name': 'MetaTagType'},
            'allow_multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'format_string': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'flatpage_meta.sitemetatag': {
            'Meta': {'object_name': 'SiteMetaTag'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_tag_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'flatpage_meta_sitemetatag_related'", 'to': "orm['flatpage_meta.MetaTagType']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meta_tag_set'", 'to': "orm['sites.Site']"})
        },
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpage_meta']