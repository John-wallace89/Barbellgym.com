from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('edit/<item_id>', views.edit_basket, name='edit_basket'),
    path('remove/<item_id>',
         views.remove_from_basket, name='remove_from_basket'),
]
