from django.contrib import admin
from carts.models import Cart

# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_field = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'product__name',]

    def user_display(self, obj):
        """A function that displays the user information.
        Parameters:
            obj: The object to display user information from.
        Returns:
            A string representing the user information or 'Анонімний користувач' if no user is present."""
        if obj.user:
            return str(obj.user)
        return 'Анонімний користувач'

    def product_display(self, obj):
        """Retrieves the name of the product associated with the given object.
        Parameters:
            obj (object): The object for which to retrieve the product name.
        Returns:
            str: The name of the product associated with the given object."""
        return str(obj.product.name)

