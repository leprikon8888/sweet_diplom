from django.db import models

from django.db import models
from ckeditor.fields import RichTextField


class PageContent(models.Model):
    page_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    text_on_page = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.page_name