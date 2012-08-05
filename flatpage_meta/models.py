from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site


class MetaTagType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    format_string = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True, null=True)
    allow_multiple = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class CommonMetaTag(models.Model):
    meta_tag_type = models.ForeignKey(
        MetaTagType,
        related_name="%(app_label)s_%(class)s_related"
    )
    content = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Meta tag"
        abstract = True

    def __unicode__(self):
        return self.meta_tag_type.format_string.format(content=self.content)


class FlatPageMetaTag(CommonMetaTag):
    flatpage = models.ForeignKey(FlatPage, related_name="meta_tag_set")

    def clean(self):
        if not self.meta_tag_type.allow_multiple:
            if FlatPageMetaTag.objects.filter(flatpage=self.flatpage, meta_tag_type=self.meta_tag_type).exclude(pk=self.pk):
                raise ValidationError("You can only have one {tag} tag per FlatPage".format(tag=self.meta_tag_type))


class SiteMetaTag(CommonMetaTag):
    site = models.ForeignKey(Site, related_name="meta_tag_set")

    def clean(self):
        if not self.meta_tag_type.allow_multiple:
            if SiteMetaTag.objects.filter(site=self.site, meta_tag_type=self.meta_tag_type).exclude(pk=self.pk):
                raise ValidationError("You can only have one {tag} tag per Site".format(tag=self.meta_tag_type))
