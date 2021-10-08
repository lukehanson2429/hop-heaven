from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_rating, name='add_rating'),
    path('edit/<int:rating_id>/', views.edit_rating, name='edit_rating'),
    path('delete/<int:rating_id>/', views.delete_rating, name='delete_rating'),
]
