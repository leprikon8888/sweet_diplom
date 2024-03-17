from django.test import TestCase
from main.models import PageContent


class PageContentModelTestCase(TestCase):
    def setUp(self):
        self.page_content = PageContent.objects.create(
            page_name='test_page',
            title='Test Page',
            content='This is a test content',
            text_on_page='<p>This is a test text on page</p>'
        )

    def test_page_content_creation(self):
        self.assertTrue(PageContent.objects.exists())

    def test_page_content_str_representation(self):
        self.assertEqual(str(self.page_content), 'test_page')