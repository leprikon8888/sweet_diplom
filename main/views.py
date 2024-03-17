from django.shortcuts import render
from django.utils.safestring import mark_safe
from main.models import PageContent


def index(request):

    context = {
        'title': 'Home - Головна',
        'content': 'Магазин білизни So Sweet Lingerie',

    }
    return render(request, 'main/index.html', context)


def about(request):
    page_content = PageContent.objects.get(page_name='about')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    page_content = PageContent.objects.get(page_name='contacts')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/contacts.html', context)


def shipping(request):
    page_content = PageContent.objects.get(page_name='shipping')
    text_on_page = mark_safe(page_content.text_on_page)  # Mark the text as safe
    context = {
        'title': page_content.title,
        'content': page_content.content,
        'text_on_page': text_on_page
    }
    return render(request, 'main/shipping.html', context)
