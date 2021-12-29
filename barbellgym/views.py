from django.shortcuts import render

# views


def error_404(request, exception):
    data = {}
    return render(request, 'barbellgym/404.html', data)


def error_500(request,  exception):
    data = {}
    return render(request, 'barbellgym/500.html', data)


def error_403(request, exception):
    data = {}
    return render(request, 'barbellgym/404.html', data)


def error_400(request,  exception):
    data = {}
    return render(request, 'barbellgym/500.html', data)