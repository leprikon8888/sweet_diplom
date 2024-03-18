from _decimal import Decimal, ROUND_HALF_UP

from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self) -> str:
        """Return a string representation of the object"""
        return self.name


class Products(models.Model):
    """The Products model represents a product in the database"""
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    is_visible = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Зображення")
    image2 = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Зображення 2")
    image3 = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Зображення 3")
    image4 = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Зображення 4")
    image5 = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Зображення 5")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Знижка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        ordering = ('id',)

    def __str__(self) -> str:
        """ Return a string representation of the object"""
        return f'{self.name} Кількість - {self.quantity}'

    def get_absolute_url(self) -> str:
        """A method that generates the absolute URL for the product using the product's slug.
        Returns a string representing the absolute URL of the product."""
        return reverse('goods:product', kwargs={'product_slug': self.slug})

    def display_id(self) -> str:
        """Return a string representation of the object"""
        return f'{self.id:05}'

    def sell_price(self) -> Decimal:
        """Calculate the selling price of the product"""
        if self.discount:
            return Decimal(str(self.price - self.price * self.discount / 100)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return Decimal(str(self.price))
