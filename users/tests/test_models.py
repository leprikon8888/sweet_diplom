from django.test import TestCase
from users.models import User


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword123',
            email='johndoe@example.com',
        )
        self.assertEqual(str(user), 'testuser')