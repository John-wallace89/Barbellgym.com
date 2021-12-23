from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.decorators.csrf import csrf_exempt

from .models import Classes, PersonalTrainers


# views
def classes(request):
    """ A view to return Barbell Classes """

    classes = Classes.objects.all()
    search = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(
                    request, "Please enter search criteria to continue")
                return redirect(reverse('barbell_classes'))

            queries = Q(
                name__icontains=search) | Q(description__icontains=search)
            products = products.filter(queries)

    context = {
        'classes': classes,
        'search_term': search,
    }

    return render(request, 'training/barbell_classes.html', context)


def personal_training(request):
    """ A view to return Barbell personal training """

    return render(request, 'training/personal_training.html')
