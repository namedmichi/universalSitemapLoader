import unittest
from src.universal_sitemap_loader import UniversalSitemapLoader
from parameterized import parameterized



# Test case class
class TestFindSitemapFunction(unittest.TestCase):

    loader = UniversalSitemapLoader()

    @parameterized.expand([
        ("https://www.muenchen.de", "https://www.muenchen.de/sitemap.xml"),
        ("https://www.tiroled.com/", "https://www.tiroled.com/de/sitemap.xml"),
        ("https://info.cern.ch", None)
    ])
    def test_find_sitemap(self, url, expected):
        self.loader.url = url
        sitemap = self.loader.find_sitemap()
        self.assertEqual(sitemap, expected)


# Run the tests
if __name__ == '__main__':
    unittest.main()
