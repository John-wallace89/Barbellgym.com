""" Views for training app """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.decorators.csrf import csrf_exempt

from .models import Classes, PersonalTrainers
from .forms import ClassesForm


# views

def classes(request):
    """ A view to return Barbell Classes """

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'training/barbell_classes.html', context)


def personal_training(request):
    """ A view to return Barbell personal training """

    p_trainers = PersonalTrainers.objects.all()

    context = {
        'p_trainers': p_trainers,
    }

    return render(request, 'training/personal_training.html', context)


@login_required
def add_class(request):
    """ A view to add a class to the site """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permisson \
            to access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES)
        if form.is_valid():
            classes = form.save()
            messages.success(request, 'Class successfully added!')
            return redirect(reverse('barbell_classes'))
        else:
            messages.error(
                request, 'Failed to add class, please ensure form is valid')
    else:
        form = ClassesForm()

    template = 'training/add_class.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_class(request, classes_id):
    """ Edit a class in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permisson to access this page.')
        return redirect(reverse('home'))

    classes = get_object_or_404(Classes, pk=classes_id)
    if request.method == 'POST':
        form = ClassesForm(request.POST, request.FILES, instance=classes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated class!')
            return redirect(reverse('barbell_classes'))
        else:
            messages.error(
                request, 'Failed to update class. \
                Please ensure the form is valid.')
    else:
        form = ClassesForm(instance=classes)
        messages.info(request, f'You are editing {classes.name}')

    template = 'training/edit_class.html'
    context = {
        'form': form,
        'classes': classes,
    }

    return render(request, template, context)


# @login_required
# def delete_product(request, product_id):
#     """ A view to delete a product """
#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, you do not have \
#         permisson to access this page.')
#         return redirect(reverse('home'))

#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()
#     messages.success(request, 'Product successfully deleted!')
#     return redirect(reverse('products'))