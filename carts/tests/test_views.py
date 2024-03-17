from django.test import TestCase, Client
from django.urls import reverse
from carts.models import Cart
from goods.models import Products, Categories
from users.models import User


class CartViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Categories.objects.create(name='Test Category')
        self.product = Products.objects.create(name='Test Product', price=10.99, category=self.category)
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=2)

    def test_cart_add_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('carts:cart_add'), {'product_id': self.product.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cart.objects.filter(user=self.user, product=self.product).first().quantity, 3)

    def test_cart_change_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('carts:cart_change'), {'cart_id': self.cart.id, 'quantity': 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Cart.objects.get(id=self.cart.id).quantity, 4)

    def test_cart_remove_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('carts:cart_remove'), {'cart_id': self.cart.id})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Cart.objects.filter(id=self.cart.id).exists())