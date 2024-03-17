import re
from django import forms


# class CreateOrderForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     phone_number = forms.CharField()
#     requires_delivery = forms.ChoiceField(
#         choices=[
#             ("0", False),
#             ("1", True),
#         ],
#     )
#     delivery_address = forms.CharField(required=False)
#     payment_on_get = forms.ChoiceField(
#         choices=[
#             ("0", 'False'),
#             ("1", 'True'),
#         ],
#     )
#
#     def clean_phone_number(self):
#         data = self.data.get('phone_number')
#         if not data:
#             return data
#
#         if not data.isdigit():
#             raise forms.ValidationError("Номер телефону повинен містити лише цифри")
#
#         pattern = re.compile(r'^(?:\+38)?0\d{9}$')
#         if not pattern.match(data):
#             raise forms.ValidationError("Невірний формат номеру")
#
#         return data
class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", 'False'),
            ("1", 'True'),
        ],
    )

    def clean_phone_number(self):
        data = self.cleaned_data.get('phone_number')
        if not data:
            return data

        pattern = re.compile(r'^(?:\+?380|0) ?\d{9}$')
        if not pattern.match(data):
            raise forms.ValidationError("Невірний формат номеру")

        return data

