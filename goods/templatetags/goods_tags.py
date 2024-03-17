from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def tag_categories():
    """A function that retrieves all categories from the Categories model"""
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """A function to change the parameters and return the updated query string"""
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)