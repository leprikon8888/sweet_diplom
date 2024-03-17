from django.test import TestCase
from django.contrib.auth import get_user_model
from carts.models import Cart
from goods.models import Categories, Products

User = get_user_model()


class CartTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.category = Categories.objects.create(name='TestCategory')
        cls.product = Products.objects.create(name='testproduct', price=100.0, category=cls.category)
        cls.cart1 = Cart.objects.create(user=cls.user, product=cls.product, quantity=2)
        cls.cart2 = Cart.objects.create(user=cls.user, product=cls.product, quantity=3)

    def test_products_price(self):
        self.assertEqual(self.cart1.products_price(), 200.0)

    def test_total_price(self):
        self.assertEqual(Cart.objects.total_price(), 500.0)

    def test_total_quantity(self):
        self.assertEqual(Cart.objects.total_quantity(), 5)

    def test_str(self):
        self.assertEqual(str(self.cart1), f'Кошик {self.user.username} | Товар {self.product.name} | Кількість {self.cart1.quantity}')