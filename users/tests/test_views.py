from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import override_settings
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

@override_settings(AUTHENTICATION_BACKENDS=['django.contrib.auth.backends.ModelBackend'])
class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword123'
        )
        self.client.force_login(self.user, backend=None)

    def test_user_registration_view(self):
        response = self.client.post(reverse('users:registration'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login_view(self):
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)

    def test_user_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_user_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)





