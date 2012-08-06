The app modifies your admin pages for Site and FlatPage to add inlines
for meta tags.

Installation
============

Add "flatpage_meta" to your INSTALLED_APPS

Usage
=====

Add the following to the HEAD of your flatpage template:

    {% load flatpage_meta_tags %}{% flatpage_meta_tags flatpage %}

or the following to your site template:

    {% load flatpage_meta_tags %}{% flatpage_meta_tags %}

Notes
=====
Some tags can be included more than once - OpenGraph arrays for instance.
These have the "allow_multiple" flag set on the tag. Otherwise we raise
a ValidationError to stop editors from making a mess.
