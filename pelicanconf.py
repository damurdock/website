#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Duncan Murdock'
SITENAME = u'Duncan Murdock'
SITEURL = 'https://duncanmurdock.name'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Github stuff for bootstrap
GITHUB_USER = 'damurdock'
GITHUB_SKIP_FORK = True

# Blogroll
LINKS =  (('Hackaday', 'https://hackaday.com/'),
          ('Adafruit', 'https://adafruit.com/'),
          ('Sparkfun', 'https://sparkfun.com/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/damurdock2'),
	('Github', 'https://www.github.com/damurdock'),
	('LinkedIn', "https://lnkd.in/bTnQP9E"),
	('Twitter', "https://twitter.com/hexome"),)

DEFAULT_PAGINATION = False

CC_LICENSE = "CC-BY-NC-SA"

TWITTER_USERNAME = "hexome"
SHARIFF_BACKEND_URL = None
SHARIFF_LANG = "en"
SHARIFF_ORIENTATION = "vertical"
SHARIFF_SERVICES = ["facebook","googleplus","twitter","mail"]
SHARIFF_THEME = "standard"
SHARIFF_TWITTER_VIA = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#####Custom#####
#DEFAULT_CATEGORY = 'misc'
TYPOGRIFY = True
PATH = 'content'
PAGE_DIR = 'pages'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
THEME = './pelican-themes/pelican-bootstrap3'
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
PYGMENTS_STYLE = 'solarizeddark'
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 500
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["render_math", "liquid_tags","i18n_subsites"]
# Most of the custom area stolen from https://github.com/razius/razius.com/blob/master/pelicanconf.py
