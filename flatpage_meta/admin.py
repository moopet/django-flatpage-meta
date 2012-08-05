from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.sites.admin import SiteAdmin as OldSiteAdmin

from flatpage_meta.models import MetaTagType, FlatPageMetaTag, SiteMetaTag


class MetaTagTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'format_string', 'allow_multiple')


class FlatPageMetaTagInline(admin.TabularInline):
    model = FlatPageMetaTag


class ReplacementFlatPageAdmin(OldFlatPageAdmin):
    inlines = [FlatPageMetaTagInline]


class SiteMetaTagInline(admin.TabularInline):
    model = SiteMetaTag


class ReplacementSiteAdmin(OldSiteAdmin):
    inlines = [SiteMetaTagInline]


admin.site.register(MetaTagType, MetaTagTypeAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ReplacementFlatPageAdmin)
admin.site.unregister(Site)
admin.site.register(Site, ReplacementSiteAdmin)
