from carts.utils import get_user_carts
from carts.models import Cart
from goods.models import Products, Categories
from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase


def dummy_get_response(request):
    return None

User = get_user_model()

class CartUtilsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Categories.objects.create(name='Test Category')
        self.product = Products.objects.create(name='Test Product', price=10.99, category=self.category)
        self.cart = Cart.objects.create(user=self.user, product=self.product, quantity=2)

    def test_get_user_carts_authenticated(self):
        request = self.factory.get('/')
        request.user = self.user  # Устанавливаем пользователя в объекте request
        carts = get_user_carts(request)
        self.assertEqual(list(carts), [self.cart])

    def test_get_user_carts_anonymous(self):
        request = self.factory.get('/')
        middleware = SessionMiddleware(dummy_get_response)
        middleware.process_request(request)
        request.session.save()

        anonymous_user = get_user_model()(  # Создаем анонимного пользователя
            username='AnonymousUser',
            email='',
            password='',
        )
        request.user = anonymous_user  # Устанавливаем анонимного пользователя в объекте request

        Cart.objects.create(session_key=request.session.session_key, product=self.product, quantity=1)
        carts = get_user_carts(request)
        self.assertEqual(len(carts), 1)
        self.assertEqual(carts.first().quantity, 1)