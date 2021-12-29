from django.shortcuts import render

# views

# Credit - https://www.youtube.com/watch?v=3SKjPppM_DU

def error_404(request, exception):
    return render(request, '404.html')


def error_403(request, exception):
    return render(request, '403.html')


def error_400(request,  exception):
    return render(request, '400.html', data)