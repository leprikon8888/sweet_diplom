from django.test import TestCase
from django.urls import reverse, resolve
from orders.views import create_order

class OrdersUrlsTestCase(TestCase):
    def test_create_order_url_resolves(self):
        url = reverse('orders:create_eorder')
        self.assertEqual(resolve(url).func, create_order)