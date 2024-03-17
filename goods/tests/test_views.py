from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from goods.models import Categories, Products


class CatalogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categories.objects.create(name='Books', slug='books')
        self.product = Products.objects.create(
            name='1984',
            category=self.category,
            slug='1984',
            price=19.99,
            quantity=5
        )

    def test_catalog_view_with_category(self):
        response = self.client.get(reverse('goods:catalog', args=['books']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1984')

    def test_catalog_view_with_search_query(self):
        response = self.client.get(reverse('goods:search'), {'q': '1984'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1984')

    def test_catalog_view_with_on_sale_filter(self):
        self.product.discount = 10.0
        self.product.save()
        response = self.client.get(reverse('goods:catalog', args=['books']), {'on_sale': 'on_sale'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1984')


class ProductViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categories.objects.create(name='Books', slug='books')

        # Создаем экземпляр SimpleUploadedFile для тестового изображения
        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'test_image_content',
            content_type='image/jpeg'
        )

        self.product = Products.objects.create(
            name='1984',
            category=self.category,
            slug='1984',
            price=19.99,
            quantity=5,
            image=test_image  # Устанавливаем тестовое изображение
        )

    def test_product_view(self):
        response = self.client.get(reverse('goods:product', args=['1984']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1984')