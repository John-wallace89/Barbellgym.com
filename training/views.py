""" Views for training app """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.decorators.csrf import csrf_exempt

from .models import Classes, PersonalTrainers
from .forms import ClassesForm, PersonalTrainerForm


# views

# Views for Class management

def classes(request):
    """ A view to return Barbell Classes """

    classes = Classes.objects.all()

    context = {
        'classes': classes,
    }

    return render(request, 'training/barbell_classes.html', context)


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


@login_required
def delete_class(request, classes_id):
    """ A view to delete a class """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have \
        permisson to access this page.')
        return redirect(reverse('home'))

    classes = get_object_or_404(Classes, pk=classes_id)
    classes.delete()
    messages.success(request, 'Class successfully deleted!')
    return redirect(reverse('barbell_classes'))


# Views for PT management


def personal_training(request):
    """ A view to return Barbell personal training """

    pt = PersonalTrainers.objects.all()

    context = {
        'pt': pt,
    }

    return render(request, 'training/personal_training.html', context)


@login_required
def add_personal_trainer(request):
    """ A view to add a PT to the site """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permisson \
            to access this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PersonalTrainerForm(request.POST, request.FILES)
        if form.is_valid():
            pt = form.save()
            messages.success(request, 'PT successfully added!')
            return redirect(reverse('personal_training'))
        else:
            messages.error(
                request, 'Failed to add PT, please ensure form is valid')
    else:
        form = PersonalTrainerForm()

    template = 'training/add_pt.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_personal_trainer(request, pt_id):
    """ Edit a PT in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have permisson to access this page.')
        return redirect(reverse('home'))

    pt = get_object_or_404(PersonalTrainers, pk=pt_id)
    if request.method == 'POST':
        form = PersonalTrainerForm(request.POST, request.FILES, instance=pt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated PT!')
            return redirect(reverse('personal_training'))
        else:
            messages.error(
                request, 'Failed to update PT. \
                Please ensure the form is valid.')
    else:
        form = PersonalTrainerForm(instance=pt)
        messages.info(request, f'You are editing {pt.name}')

    template = 'training/edit_pt.html'
    context = {
        'form': form,
        'pt': pt,
    }

    return render(request, template, context)


@login_required
def delete_personal_trainer(request, pt_id):
    """ A view to delete a PT """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you do not have \
        permisson to access this page.')
        return redirect(reverse('home'))

    pt = get_object_or_404(PersonalTrainers, pk=pt_id)
    pt.delete()
    messages.success(request, 'PT successfully deleted!')
    return redirect(reverse('personal_training'))
