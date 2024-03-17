from django import template
from carts.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def user_carts(request):
    """  A function that retrieves the user's carts.
    Parameters:
        request (HttpRequest): The HTTP request object."""
    return get_user_carts(request)
