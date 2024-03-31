from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

def login(request):
    """ A function to handle user login. It takes a request object as a parameter and performs
    authentication and form validation. """
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(
                username=username,
                password=password,
                backend='django.contrib.auth.backends.ModelBackend'
            )

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, _('%(username)s, Ви увійшли до облікового запису') % {'username': username})  # Используем gettext_lazy с форматированием строк

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': _('Home - Авторизація'),  # Используем gettext_lazy
        'form': form
    }
    return render(request, 'users/login.html', context)



def registration(request):
    """A function that handles user registration"""
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            user = authenticate(username=user.username, password=form.cleaned_data['password1'],
                                backend='django.contrib.auth.backends.ModelBackend')
            if user is not None:
                auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(request, _(f'{user.username}, Ви успішно зареєструвалися та увійшли до облікового запису'))  # Используем gettext
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': _('Home - Реєстрація'),  # Используем gettext
        'form': form
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    """A view function to handle the user profile, allowing them to update their profile information
    and displaying their order history."""
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _('профіль успішно оновлено'))  # Используем gettext
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'username': request.user.username,
            'email': request.user.email,
        }
        form = ProfileForm(instance=request.user, initial=initial_data)

    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    'orderitem_set',
                    queryset=OrderItem.objects.select_related('product'),
                )
            ).order_by('-id')
    )

    context = {
        'title': _('Home - Кабінет'),  # Используем gettext
        'form': form,
        'orders': orders,
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    """A view function to display the user's cart"""
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    """A view function to logout the user"""
    username = request.user.username
    logout_message_part1 = _("{username}").format(username=username)
    logout_message_part2 = _("Ви вийшли з облікового запису")
    logout_message = f"{logout_message_part1} {logout_message_part2}"
    messages.success(request, logout_message)
    auth.logout(request)
    return redirect(reverse('main:index'))