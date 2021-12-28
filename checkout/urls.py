"""
Urls for checkout app
"""

from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>',
        views.checkout_success,
        name='checkout_success'),
    path(
        'save_checkout_data/',
        views.save_checkout_data,
        name='save_checkout_data'),
    path('webhook/', webhook, name='webhook'),
]
