from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Головна',
        'content': 'Магазин білизни So Sweet Lingerie',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'text_on_page': 'Текст про то, що наша білизна найкраща'

    }
    return render(request, 'main/about.html', context)