from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
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

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Замовлення оформлено!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
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


def test_create_order_view_post(self):
    form_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'phone_number': '+380991234567',
        'requires_delivery': '1',
        'delivery_address': 'Test Address',
        'payment_on_get': '0',
    }

    response = self.client.post(reverse('create_order'), data=form_data)

    # Проверка статуса ответа
    if response.status_code != 302:
        print(response.content)  # Вывод содержимого ответа в консоль

    self.assertRedirects(response, reverse('user:profile'))

