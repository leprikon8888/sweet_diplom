from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.forms import UserRegistrationForm, UserLoginForm, ProfileForm
from users.models import User

User = get_user_model()

class UserRegistrationFormTestCase(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_registration_form(self):
        form_data = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': 'invalidemail',
            'password1': 'short',
            'password2': 'short',
        }
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserLoginFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
        )

    def test_valid_login_form(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        form = UserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_login_form(self):
        form_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        form = UserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class ProfileFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
        )

    def test_valid_profile_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'testuser',
            'email': 'johndoe@example.com',
        }
        form = ProfileForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_profile_form(self):
        form_data = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': 'invalidemail',
        }
        form = ProfileForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())