"""
Universal Sitemap Loader
~~~~~~~~~~~~~~~~~~~~~

Package for loading sitemaps from any website.
Basic usage:

   >>> from universal_sitemap_loader import UniversalSitemapLoader
   >>> loader = UniversalSitemapLoader("https://www.example.com/")
   >>> sitemap = loader.find_sitemap()


:license: GPLv3, see LICENSE for more details.
:author: Michael Selbertinger
"""

from .__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __version__,
)
from .sitemapLoader import (
    UniversalSitemapLoader
)