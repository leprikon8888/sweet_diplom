import re
from django import forms
from django.test import TestCase
from orders.forms import CreateOrderForm


class CreateOrderFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '+380991234567',
            'requires_delivery': '1',
            'delivery_address': 'Test Address',
            'payment_on_get': '0',
        }
        form = CreateOrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_phone_number(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': 'invalid_number',
            'requires_delivery': '1',
            'delivery_address': 'Test Address',
            'payment_on_get': '0',
        }
        form = CreateOrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)

    def clean_phone_number(self):
        data = self.data.get('phone_number')  # Используем self.data вместо self.cleaned_data
        if not data:
            return data

        print(f"Validating phone number: {data}")

        if not data.isdigit():
            print("Phone number contains non-digit characters")
            raise forms.ValidationError("Номер телефону повинен містити лише цифри")

        pattern = re.compile(r'^(?:\+38)?0\d{9}$')
        if not pattern.match(data):
            print("Phone number format is incorrect")
            raise forms.ValidationError("Невірний формат номеру")

        print("Phone number is valid")
        return data

    def test_valid_form(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '+380991234567',
            'requires_delivery': '1',
            'delivery_address': 'Test Address',
            'payment_on_get': '0',
        }
        form = CreateOrderForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # Выводим ошибки валидации
        self.assertTrue(form.is_valid())