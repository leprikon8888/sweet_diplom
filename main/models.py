from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class PageContent(models.Model):
    page_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    text_on_page = CKEditor5Field('Text', config_name='extends', blank=True, null=True)

    def __str__(self):
        return self.page_name
