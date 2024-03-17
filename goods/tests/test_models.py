from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from goods.models import Categories, Products


class CategoryModelTests(TestCase):
    def setUp(self):
        Categories.objects.all().delete()  # Очищаем таблицу категорий перед каждым тестом

    def test_category_string_representation(self):
        category = Categories.objects.create(name='Books')
        self.assertEqual(str(category), 'Books')


class ProductModelTests(TestCase):
    def setUp(self):
        Categories.objects.all().delete()  # Очищаем таблицу категорий перед каждым тестом
        Products.objects.all().delete()  # Очищаем таблицу продуктов перед каждым тестом

        self.category = Categories.objects.create(name='Technology')
        self.product = Products.objects.create(
            name='1984',
            category=self.category,
            price=19.99,
            discount=10.0,
            quantity=5
        )

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), '1984 Кількість - 5')

    def test_product_get_absolute_url(self):
        expected_url = reverse('goods:product', kwargs={'product_slug': self.product.slug})
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    def test_product_display_id(self):
        self.assertEqual(self.product.display_id(), f'{self.product.id:05}')

    def test_product_sell_price_with_discount(self):
        self.assertEqual(self.product.sell_price(), Decimal('17.99'))

    def test_product_sell_price_without_discount(self):
        self.product.discount = 0.0
        self.assertEqual(self.product.sell_price(), Decimal(str(self.product.price)))