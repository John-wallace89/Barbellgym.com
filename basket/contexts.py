"""
Context for basket app
"""

from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    """
    Function for calculating basket total
     and quantity for products with and
     without sizes.
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

# For if products without sizes are added to store in future
    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context
