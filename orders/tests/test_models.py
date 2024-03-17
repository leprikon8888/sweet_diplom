from django.contrib.auth import get_user_model
from django.test import TestCase

from goods.models import Products, Categories
from orders.models import Order, OrderItem

User = get_user_model()


class OrderModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            first_name='Test',
            last_name='User',
        )
        self.category = Categories.objects.create(name='Test Category')

        self.product = Products.objects.create(
            name='Test Product',
            price=10.0,
            quantity=10,
            category=self.category,  # Присваиваем созданную категорию
        )

    def test_order_creation(self):
        order = Order.objects.create(
            user=self.user,
            phone_number='+380991234567',
            requires_delivery=True,
            delivery_address='Test Address',
            payment_on_get=False,
        )
        self.assertEqual(
            str(order),
            f'Замовлення № {order.pk} | Покупець {self.user.first_name} {self.user.last_name}')

    def test_order_item_creation(self):
        order = Order.objects.create(
            user=self.user,
            phone_number='+380991234567',
            requires_delivery=True,
            delivery_address='Test Address',
            payment_on_get=False,
        )
        order_item = OrderItem.objects.create(
            order=order,
            product=self.product,
            name=self.product.name,
            price=self.product.sell_price(),
            quantity=2,
        )
        self.assertEqual(order_item.products_price(), 20.0)
        self.assertEqual(
            str(order_item), f'Товар {order_item.name} | Замовлення № {order_item.order.pk}')
