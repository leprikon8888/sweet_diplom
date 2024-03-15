from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Головна',
        'content': 'Магазин білизни So Sweet Lingerie',

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Текст про то, що наша білизна найкраща'

    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Home - Контакти',
        'content': 'Контакти',
        'text_on_page': 'Текст про то, що наша білизна найкраща'

    }
    return render(request, 'main/contacts.html', context)


def shipping(request):
    context = {
        'title': 'Home - Доставка',
        'content': 'Доставка',
        'text_on_page': 'Текст про то, що наша білизна найкраща'

    }
    return render(request, 'main/shipping.html', context)