from django import template


register = template.Library()


@register.filter(name='get_subtotal')
def get_subtotal(price, quantity):
    return price * quantity
