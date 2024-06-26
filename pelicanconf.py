#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import logging

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.
import shutil
from datetime import datetime

import m

#  from pelican_jupyter import markup
#  from pelican.plugins import webring
# from pelican.plugins import liquid_tags
#  from pelican.plugins import myst_reader
from pelican.plugins import pelican_redirect, sitemap
from pelican_ashwinvis import FEDIAPI, FEDIHOST, FEDIUSER, post_stats
from pelican_ashwinvis.util.util import read_opml

AUTHOR = "Ashwin Vishnu Mohanan"
SITENAME = "Ashwin Vishnu's Website"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Stockholm"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Metadata
DEFAULT_METADATA = {
    "author": AUTHOR,
    "category": "Blog",
    "summary": "",  # Disable auto-generated summary
    # TODO:
    # 'status': 'draft',  # Avoid accidently publishing articles
}

THEME = "m.css/pelican-theme"
THEME_STATIC_DIR = "static"
STATIC_PATHS = ["images", "pdf", "static", "media"]
EXTRA_PATH_METADATA = {
    f"extra/{resource}": {"path": resource}
    for resource in (
        "robots.txt",
        "manifest.webmanifest",
        "sw.js",
        "app.js",
    )
}
STATIC_PATHS.extend(EXTRA_PATH_METADATA)

DIRECT_TEMPLATES = (
    "index",
    "tags",
    "categories",
    "archives",
    # Requires tipue_search
    #  "search",
    # Requires pybtex
    #  "publications",
)

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "m-code"},
        "markdown.extensions.toc": {"anchorlink": True},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

M_CSS_FILES = [
    "/static/custom.compiled.css",
    "/static/webmention.css",
    "/static/fedicomments.css",
]
M_THEME_COLOR = "#22272e"

with open("templates/header.html") as header:
    M_HTML_HEADER = header.read()

PLUGINS = [m.htmlsanity, m.components, m.code, m.metadata]  # , myst_reader]

M_SITE_LOGO = "/images/logo_ashwin.png"
M_SITE_LOGO_TEXT = "fluid.quest"
M_FAVICON = (M_SITE_LOGO, "image/png")
M_BLOG_FAVICON = M_FAVICON


# m.metadata
FORMATTED_FIELDS = ["description", "badge"]

# Navbar
M_LINKS_NAVBAR1 = [
    (
        "✍️ Posts",
        "archives.html",
        "[blog]",
        [
            ("Blog", "category/blog.html", ""),
            ("Tech Talk", "category/tech-talk.html", ""),
        ],
    ),
    (
        "📫 Subscribe",
        "pages/subscribe.html",
        "[subscribe]",
        [
            ("Feeds: All", "feeds/all.atom.xml", ""),
            ("Feeds: Blog", "feeds/blog.atom.xml", ""),
            ("Feeds: Microblog", "feeds/microblog.atom.xml", ""),
            ("Feeds: Tech Talk", "feeds/tech-talk.atom.xml", ""),
        ],
    ),
]

M_LINKS_NAVBAR2 = [
    (
        "✨Showcase",
        "/#what-i-do",
        "",
        [
            ("CV", "pages/cv.html", ""),
            ("Research", "pages/research.html", ""),
            ("Software", "pages/software.html", ""),
            (
                "Talks",
                "talks",
                "[talks]",
            ),
        ],
    ),
    ("🖖Sponsors", "pages/sponsors.html", "[sponsors]", []),
    ("🪐Planet", "pages/planet.html", "[planet]", []),
    ("📧Contact", "pages/contact.html", "[contact]", []),
]
M_LINKS_FOOTER1 = [
    ("Social", ""),
    ("LinkedIn", "https://www.linkedin.com/in/ashwinvishnu/"),
    ("Mastodon [personal]", "https://mastodon.acc.sunet.se/@ashwinvis"),
    ("Mastodon [science]", "https://fediscience.org/@ashwinvis"),
    ("Matrix", "https://matrix.to/#/@ashwinvis:matrix.org"),
    ("Pixelfed [photos]", "https://pixelfed.social/ashwinvis"),
    ("Peertube [videos]", "https://tube.tchncs.de/a/ashwinvis/video-channels"),
]
M_LINKS_FOOTER2 = [
    ("Research", ""),
    ("Google-Scholar", "https://scholar.google.se/citations?user=zv4wwKoAAAAJ"),
    ("ORCID", "https://orcid.org/0000-0002-2979-6327"),
    ("ResearchGate", "https://www.researchgate.net/profile/Ashwin-Vishnu-Mohanan-2"),
    ("Zenodo", "https://zenodo.org/search?page=1&size=20&q=Mohanan,%20Ashwin%20Vishnu"),
    ("Zotero", "https://zotero.org/ashwinvis"),
]
M_LINKS_FOOTER3 = [
    ("Code", ""),
    ("Codeberg", "https://codeberg.org/ashwinvis"),
    ("GitHub", "https://github.com/ashwinvis"),
    ("Gitlab", "https://source.coderefinery.org/ashwinvis/"),
    ("Heptapod", "https://foss.heptapod.net/avmo"),
]
M_LINKS_FOOTER4 = (
    [
        ("Sitemap", ""),
        M_LINKS_NAVBAR1[1][:2],
    ]
    + [(title, url) for title, url, _ in M_LINKS_NAVBAR1[1][3]]
    + [(title, url) for title, url, _, _ in M_LINKS_NAVBAR2]
)

with open("templates/footer.rst") as footer:
    M_FINE_PRINT = footer.read().format(year=datetime.now().year)

with open("templates/archived_badge.rst") as badge:
    M_ARCHIVED_ARTICLE_BADGE = badge.read()

# For landing page
FORMATTED_FIELDS = ["summary", "landing", "header", "footer", "description", "badge"]
M_NEWS_ON_INDEX = ("Latest posts", 5)

# TODO:
M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True

if not shutil.which("latex"):
    logging.warning("LaTeX not found, fallback to rendering math as code")
    M_MATH_RENDER_AS_CODE = True

# The first article is by default fully expanded on index and archive page.
# This disables it
M_COLLAPSE_FIRST_ARTICLE = True

#  M_BRIDGY_PUBLISH = "mastodon"

M_WEBMENTIONS = True

M_FEDICOMMENTS = True
M_FEDIHOST = FEDIHOST
M_FEDIAPI = FEDIAPI
M_FEDIUSER = FEDIUSER

PLUGINS += [
    #  webring,
    post_stats,
    pelican_redirect,
    sitemap,
    #  liquid_tags,
    #  markup,
    # "representative_image",
    # "tipue_search",
    # "pelican_bibtex",
]

# ipynb
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_MARKUP_USE_FIRST_CELL = True
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False

# pelican_planet / webring
PLANET_FEEDS = read_opml("planet.opml", ["Planets"])
PLANET_TEMPLATE = "templates/planet.md.j2"
PLANET_PAGE = "content/pages/planet.md"
PLANET_MAX_ARTICLES_PER_FEED = 1
PLANET_MAX_ARTICLES = max(42, PLANET_MAX_ARTICLES_PER_FEED * len(PLANET_FEEDS))
PLANET_MAX_SUMMARY_LENGTH = 140
PLANET_MAX_AGE_IN_DAYS = 21

WEBRING_FEED_URLS = list(PLANET_FEEDS.values())
WEBRING_ARTICLES_PER_FEED = PLANET_MAX_ARTICLES_PER_FEED
WEBRING_MAX_ARTICLES = max(42, WEBRING_ARTICLES_PER_FEED * len(WEBRING_FEED_URLS))
WEBRING_SUMMARY_LENGTH = 140
# TEMPLATE_PAGES = {"planet.html": "planet.html"}

# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.5,
        "pages": 0.8,
    },
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# liquid_tags
YOUTUBE_THUMB_ONLY = True

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# Publications with pybtex
PUBLICATIONS_SRC = "content/static/CV.bib"

# HTML Template
#  PAGINATED_TEMPLATES = ("category", "archives", "index", "pages")
DIRECT_TEMPLATES = (
    "index",
    "tags",
    "categories",
    "archives",
    # Requires tipue_search
    #  "search",
    # Requires pybtex
    #  "publications",
)

AV_THEME = ""

if AV_THEME == "light":
    M_CSS_FILES.insert(0, "/static/m-light.css")
    IPYNB_COLORSCHEME = "solarized-light"
elif AV_THEME == "dark":
    M_CSS_FILES.insert(0, "/static/m-dark.css")
    M_CSS_FILES.append("/static/bibbase-m-dark.css")
    IPYNB_EXPORT_TEMPLATE = "nbconvert.tpl"
    IPYNB_COLORSCHEME = "monokai"
else:
    M_CSS_FILES.insert(0, "/static/m-unified.css")
