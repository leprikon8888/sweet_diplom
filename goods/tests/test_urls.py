from django.test import TestCase
from django.urls import reverse, resolve
from goods.views import catalog, product


class URLsTestCase(TestCase):
    def test_catalog_url(self):
        url = reverse('goods:catalog', args=['books'])
        self.assertEqual(resolve(url).func, catalog)

    def test_product_url(self):
        url = reverse('goods:product', args=['1984'])
        self.assertEqual(resolve(url).func, product)

    def test_search_url(self):
        url = reverse('goods:search')
        self.assertEqual(resolve(url).func, catalog)