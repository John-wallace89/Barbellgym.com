from django.urls import path
from . import views

urlpatterns = [
    path('barbell_classes/', views.classes, name='barbell_classes'),
    path('personal_training/', views.personal_training, name='personal_training'),
    path('add_class/', views.add_class, name='add_class'),
    # path('add_pt/', views.add_pt, name='add_pt'),
    # path('edit_class/<int:classes_id>', views.edit_class, name='edit_class'),
    # path('edit/<int:personaltrainer_id>', views.edit_pt, name='edit_pt'),
    # path('delete/<int:classes_id>/', views.delete_class, name='delete_class'),
    # path('delete/<int:product_id>/', views.delete_pt, name='delete_pt'),
]
