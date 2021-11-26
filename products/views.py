from django.shortcuts import render
from .models import Product

# Views
def products(request):
    """ A view to show products in the barbell shop """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
