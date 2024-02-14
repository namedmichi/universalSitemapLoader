import requests
from urllib.parse import urljoin
import xml.etree.ElementTree as ET
import gzip
import io
import requests
from urllib.parse import urljoin
import gzip
import io
from typing import List

import xml.etree.ElementTree as ET


class UniversalSitemapLoader:
    COMMON_PATHS = ["sitemap.xml", "sitemap_index.xml", "sitemap1.xml", "sitemap", "sitemap_index", "sitemap"]

    def __init__(self, url: str=None):
        self.url = url

    def try_url(self, path):
        try:
            response = requests.get(path, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                return response
        except requests.RequestException:
            return None

    def find_sitemap(self) -> str:
        """Find the sitemap on the given website from the UniversalSitemapLoader.url

:return: The URL of the sitemap or None if no sitemap was found.	

Usage::


>>> from universal_sitemap_loader import UniversalSitemapLoader
>>> loader = UniversalSitemapLoader("https://www.example.com/")
>>> sitemap = loader.find_sitemap()
>>> sitemap
https://www.example.com/sitemap.xml
        """
        if self.url is None:
            return None

        for path in self.COMMON_PATHS:
            full_path = urljoin(self.url, path)
            content = self.try_url(full_path)

            if content and content.url == full_path and content.text:
                print(f"Sitemap found at: {full_path}")
                return full_path

            if content and self.url != content.url:
                print(f"Redirected to: {content.url}")
                self.url = content.url
                return self.find_sitemap()

        print("No sitemap found.")

    def get_urls_from_sitemap(self, sitemap_url: str = None, urls: List[str] = None) -> List[str]:
        """Get all URLs from the sitemap, even with compressed or nested sitemaps.
:param sitemap_url: The URL of the sitemap.
:param urls: The list of URLs to append to.
:return: The list of URLs from the sitemap.

Usage::

>>> from universal_sitemap_loader import UniversalSitemapLoader
>>> loader = UniversalSitemapLoader()
>>> urls = loader.get_urls_from_sitemap("https://www.example.com/sitemap.xml")

        """
        if urls is None:
            urls = []

        if sitemap_url is None:
            sitemap_url = self.find_sitemap()

        try:
            response = requests.get(sitemap_url, stream=True)
            if response.status_code != 200:
                return [f"Failed to retrieve sitemap: HTTP {response.status_code}"]

            if sitemap_url.endswith('.gz'):
                with gzip.open(io.BytesIO(response.content)) as f:
                    content = f.read()
            else:
                content = response.content

            root = ET.fromstring(content)

            for loc in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
                url = loc.text
                if url.endswith('.xml') or url.endswith('.xml.gz'):
                    self.get_urls_from_sitemap(url, urls)
                else:
                    urls.append(url)

            return urls

        except requests.RequestException as e:
            return [f"An error occurred: {e}"]
        except ET.ParseError as e:
            return [f"Failed to parse sitemap XML: {e}"]
        except Exception as e:
            return [f"An unexpected error occurred: {e}"]

    def get_urls(self) -> List[str]:
        """Get all URLs from the sitemap, even with compressed or nested sitemaps.
:return: The list of URLs from the sitemap.

Usage::

>>> from universal_sitemap_loader import UniversalSitemapLoader
>>> loader = UniversalSitemapLoader("https://www.example.com/")
>>> urls = loader.get_urls_from_sitemap()
        """
        sitemap_url = self.find_sitemap()
        return self.get_urls_from_sitemap(sitemap_url)



if __name__ == '__main__':

    loader = UniversalSitemapLoader("https://www.ecoservice24.com")
    sitemap = loader.find_sitemap()