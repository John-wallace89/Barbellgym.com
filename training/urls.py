""" URLS for training app """

from django.urls import path
from . import views

urlpatterns = [
    path('barbell_classes/', views.classes, name='barbell_classes'),
    path('personal_training/', views.personal_training, name='personal_training'),
    path('add_class/', views.add_class, name='add_class'),
    path('edit_class/<int:classes_id>/', views.edit_class, name='edit_class'),
    path('delete/<int:classes_id>/', views.delete_class, name='delete_class'),
]
