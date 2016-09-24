#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

authors = ['Jaan Tollander de Balsch',
           'Aapo Haavisto',
           'Oskari Karkkinen',
           'Tapani Koistinen',
           'Lauri Seppäläinen',
           'Juhani Sipilä',
           'Markus Tyrkkö', ]

AUTHOR = "\n".join(authors)
del authors
SITENAME = '3D Modelling of Environment with Stereo Vision'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# (name, url)
LINKS = (
    ('GitHub Repository', 'https://github.com/jaantollander/SCI-C1000'),
)

# Social widget
SOCIAL = (
    ('', '#'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Non default settings
# http://docs.getpelican.com/en/3.6.3/settings.html
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins
# http://docs.getpelican.com/en/3.6.3/plugins.html#plugins
# https://github.com/getpelican/pelican-plugins
PLUGINS = []
PLUGIN_PATHS = []
