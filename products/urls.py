from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_r/<int:product_id>/', views.add_product_rating, name='add_product_rating'),
    path('edit_r/<int:rating_id>/', views.edit_product_rating, name='edit_product_rating'),
    path('delete_r/<int:rating_id>/', views.delete_product_rating, name='delete_product_rating'),
]
