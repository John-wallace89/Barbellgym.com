from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# views


def products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    search = None

    if request.GET:
        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(
                    request, "Please enter search criteria to continue")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=search) | Q(description__icontains=search)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
