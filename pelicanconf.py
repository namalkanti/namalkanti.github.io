#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Niraj Amalkanti'
SITENAME = 'Mitigating Failure'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

THEME = 'themes/pelican-mg/'
SITESUBTITLE = SITENAME

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

SOCIAL = (('github', 'https://github.com/namalkanti'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
