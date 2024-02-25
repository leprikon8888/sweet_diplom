from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Головна',
        'content': 'Магазин білизни So Sweet Lingerie'
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Текст про то, що наша білизна найкраща'

    }
    return render(request, 'main/about.html', context)