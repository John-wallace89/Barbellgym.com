from django.shortcuts import render


# views
def contact_us(request):
    """ A view to return Index page """

    return render(request, 'contact/contact_us.html')
