from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    #
    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": "form-control mt-3"}), required=False
    # )
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваше имя пользователя",
    #         }
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите ваш email *youremail@example.com",
    #             # 'readonly': True,
    #         }
    #     ),
    # )