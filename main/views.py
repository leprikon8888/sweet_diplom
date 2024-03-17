from django.shortcuts import render
from django.utils.safestring import mark_safe
from main.models import PageContent


def index(request):
    """A function that renders the main index page with a specific context."""
    context = {
        'title': 'Home - Головна',
        'content': 'Магазин білизни So Sweet Lingerie',

    }
    return render(request, 'main/index.html', context)


def about(request):
    """Retrieves the page content for the 'about' page and renders it using the 'main/about.html' template."""
    page_content = PageContent.objects.get(page_name='about')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    """Retrieves the page content for the 'contacts' page and renders it using the 'main/contacts.html' template."""
    page_content = PageContent.objects.get(page_name='contacts')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/contacts.html', context)


def shipping(request):
    """This function retrieves the 'shipping' page content from the database and renders it using the 'shipping.html'"""
    page_content = PageContent.objects.get(page_name='shipping')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/shipping.html', context)
