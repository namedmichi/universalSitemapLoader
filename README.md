# Universal Sitemap Loader

**Universal Sitemap Loader** the easiest way to find a Sitemap

```python
   >>> from universal_sitemap_loader import UniversalSitemapLoader
   >>> loader = UniversalSitemapLoader("https://www.example.com/")
   >>> sitemap = loader.find_sitemap()
```

This tries to find the Sitemap no matter where the heck it is.

## Key Features

-   Can handel compressed (.gz) files
-   Recursively gets the URL´s from all sitemaps
-   tries to find even the strangest placed sitemaps

Other functions include:

```python
>>> urls = loader.get_urls()
or
>>> urls = loader.get_urls_from_sitemap("https://www.example.com/sitemap.xml")
```

## Installing the Package

Universal Sitemap Loader is available on PyPI:

```console
$ python -m pip install universal-sitemap-loader
```

Officially supports Python 3.7+.

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details
