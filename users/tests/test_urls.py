from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import login, registration, profile, users_cart, logout


class TestUrls(SimpleTestCase):

    def test_login_url_resolves(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func, login)

    def test_registration_url_resolves(self):
        url = reverse('users:registration')
        self.assertEqual(resolve(url).func, registration)

    def test_profile_url_resolves(self):
        url = reverse('users:profile')
        self.assertEqual(resolve(url).func, profile)

    def test_users_cart_url_resolves(self):
        url = reverse('users:users_cart')
        self.assertEqual(resolve(url).func, users_cart)

    def test_logout_url_resolves(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func, logout)