from django.test import TestCase, Client
from django.urls import reverse
from main.models import PageContent


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.page_content = PageContent.objects.create(
            page_name='about',
            title='About Us',
            content='This is the about page content',
            text_on_page='<p>This is the about page text</p>'
        )

    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/about.html')
        self.assertContains(response, self.page_content.title)
        self.assertContains(response, self.page_content.content)
        self.assertContains(response, self.page_content.text_on_page)

