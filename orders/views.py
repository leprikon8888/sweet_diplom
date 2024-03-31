from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from orders.utils import send_order_to_telegram
import asyncio

@login_required
def create_order(request):
    """
    A view function that handles the creation of an order.
    If the request method is POST, it processes the form data, creates an order,
    adds order items, updates product quantities, clears the user's cart,
    and displays success messages before redirecting to the user's profile page.
    """
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                            first_name=form.cleaned_data['first_name'],  # Добавлено
                            last_name=form.cleaned_data['last_name'],    # Добавлено
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостатня кількість товару {name} на складі\
                                                       В наявності - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        # Отправить информацию о заказе в Телеграм
                        try:
                            (send_order_to_telegram(order))
                        except Exception as e:
                            messages.error(request, f"Ошибка при отправке сообщения в Телеграм: {str(e)}")

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, "Замовлення оформлено! Найближчим часом вами зв'яжеться наш менеджер")
                        return redirect('user:profile')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('cart:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Home - Оформлення замовлення',
        'form': form,
        'order': True,
    }
    return render(request, 'orders/create_order.html', context=context)