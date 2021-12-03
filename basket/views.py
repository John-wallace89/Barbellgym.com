from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# views


def view_basket(request):
    """ A view to return basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of products to the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated quantity of {product.name} to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """ A view to adjust quantity in the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size'][size]:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated quantity of {product.name} to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ To remove products in the basket in the basket """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
