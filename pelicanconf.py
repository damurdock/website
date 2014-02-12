#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Duncan Murdock'
SITENAME = u'Duncan Murdock'
SITEURL = 'HTTP://duncanmurdock.herokuapp.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#####Custom#####
DEFAULT_CATEGORY = 'misc'
TYPOGRIFY = True
PATH = 'content'
PAGE_DIR = 'pages'
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
ARTICLE_URL = ('articles/{slug}/')
ARTICLE_SAVE_AS = ('articles/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False

# Most of the custom area stolen from https://github.com/razius/razius.com/blob/master/pelicanconf.py