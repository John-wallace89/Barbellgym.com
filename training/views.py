from django.shortcuts import render


# views
def classes(request):
    """ A view to return Barbell Classes """

    return render(request, 'training/barbell_classes.html')


def personal_training(request):
    """ A view to return Barbell personal training """

    return render(request, 'training/personal_training.html')
