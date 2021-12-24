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
