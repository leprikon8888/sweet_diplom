from django.http import JsonResponse
from django.template.loader import render_to_string
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


def cart_add(request):
    """A function to add a product to the shopping cart for a user, either authenticated or using a session"""
    product_id = request.POST.get('product_id')
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': user_cart}, request=request)

    response_data = {
        'message': 'Товар додан до кошика',
        'cart_items_html': cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request):
    """A function that handles changes to the user's shopping cart"""
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)

    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity": updated_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    """ A function to remove an item from the cart and return a JSON response.
    Parameters:
    - request: the HTTP request object containing the POST data with the cart_id
    Returns:
    - JsonResponse: a JSON response containing a message, updated cart items HTML, and the quantity of items deleted"""
    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts':user_cart}, request=request)

    response_data = {
        'message': 'Товар видалено',
        'cart_items_html': cart_items_html,
        'quantity_deleted': quantity,
    }

    return JsonResponse(response_data)
