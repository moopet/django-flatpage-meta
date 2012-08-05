The app modifies your admin pages for Site and FlatPage to add inlines
for meta tags.

Installation
============

Add "flatpage_meta" to your INSTALLED_APPS

Usage
=====

Some tags can be included more than once - OpenGraph arrays for instance.
These have the "allow_multiple" flag set on the tag. Otherwise we raise
a ValidationError to stop editors from making a mess.
