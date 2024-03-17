from typing import Optional
from django.db import models
from goods.models import Products
from users.models import User


class CartQueryset(models.QuerySet):
    """A custom queryset for the Cart model"""
    def total_price(self):
        """Calculate the total price of all products in the cart.
        No parameters. Returns the total price as a float."""
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        """A function to calculate the total quantity of items in the shopping cart"""
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    """Model representing a shopping cart"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Користувач')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')

    class Meta:
        db_table = 'cart'
        verbose_name = "Кошик"
        verbose_name_plural = "Кошик"

    objects = CartQueryset().as_manager()

    def products_price(self) -> Optional[float]:
        """Calculate and return the total price of the products based on the sell price and quantity"""
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self) -> str:
        """Returns a string representation of the object"""
        if self.user:
            return f'Кошик {self.user.username} | Товар {self.product.name} | Кількість {self.quantity}'
        return f'Анонімний кошик| Товар {self.product.name} | Кількість {self.quantity}'