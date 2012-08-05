from django import template
from django.contrib.sites.models import Site

register = template.Library()

@register.inclusion_tag('flatpage_meta_tags.html')
def flatpage_meta_tags(flatpage=None):
    flatpage_tags = flatpage.meta_tag_set.all() if flatpage else None
    site_tags = Site.objects.get_current().meta_tag_set.all()
    if flatpage_tags:
        site_tags = site_tags.exclude(meta_tag_type__in=[f.meta_tag_type for f in flatpage_tags])

    return {
        'site_tags': site_tags,
        'flatpage_tags': flatpage_tags,
    }
