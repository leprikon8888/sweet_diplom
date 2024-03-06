from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Будь ласка, введіть правильні ім'я користувача та пароль. Обидва поля можуть бути чутливими до регістру",
        'inactive': "Цей обліковий запис неактивний",
    }

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

# username = forms.CharField(
#     label="Ім'я",
#     widget=forms.TextInput(attrs={"autofocus": True,
#                                   'class': 'form-control',
#                                   'placeholder': "Введіть ваше ім'я"})
# )
# password = forms.CharField(
#     label='Пароль',
#     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
#                                       'class': 'form-control',
#                                       'placeholder': "Введіть ваш пароль"})
# )
#
# class Meta:
#     model = User
#     fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()