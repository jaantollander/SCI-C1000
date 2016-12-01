#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = ['Jaan Tollander de Balsch',
           'Aapo Haavisto',
           'Oskari Karkkinen',
           'Tapani Koistinen',
           'Lauri Seppäläinen',
           'Juhani Sipilä',
           'Markus Tyrkkö', ]

AUTHOR = 'Jaan Tollander de Balsch'
SITENAME = 'Indoor Navigation from Multiple Images'
SITESUBTITLE = 'Finding the way'  # Subtitle that appears below sitename
SITEURL = 'https://jaantollander.github.io/SCI-C1000'
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True


PATH = 'content'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/Helsinki'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# (name, url)
# LINKS = (
#     ('', '#'),
# )

# Social widget
GITHUB_URL = 'https://github.com/jaantollander'
SOCIAL = (
    ('GitHub Repository', 'https://github.com/jaantollander/SCI-C1000'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# SETTINGS
MENUITEMS = [
    ('Home Page', 'index.html'),
]
STATIC_PATHS = [
    'images',
    'figures',
    'downloads',
    'tables',
    'favicon.png',
    'logo.png'
]

# Themes and Plugins
THEME = 'pelican-themes/octopress'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'render_math',
    'better_tables',
    # 'better_figures_and_images',
    'pelican_youtube',
]

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

SIDEBAR_IMAGE = "logo.png"
SIDEBAR_IMAGE_ALT = "logo"
