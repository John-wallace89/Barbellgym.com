from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('', views.personal_training, name='personal_trainers'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
