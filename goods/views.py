from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products
from goods.utils import q_search


def catalog(request, category_slug=None):
    """A view function for rendering a catalog page with the option to filter by category, search query, and sale items.
     Parameters:
     - request: HttpRequest object
     - category_slug: str, optional category slug for filtering the products"""
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query is not None and query.strip():  # Проверяем, что параметр q присутствует и строка запроса не пуста
        goods = q_search(query)
    elif category_slug:  # Добавляем проверку на наличие category_slug
        category = get_object_or_404(Categories, slug=category_slug)
        goods = Products.objects.filter(category=category)
    else:
        goods = Products.objects.none()  # Если category_slug пуст, возвращаем пустой QuerySet

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
        'query': query,  # Передаем строку запроса в контекст
        'is_search': query is not None  # Добавляем флаг, указывающий, был ли выполнен поиск
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {'product': product}

    return render(request, 'goods/product.html', context=context)
