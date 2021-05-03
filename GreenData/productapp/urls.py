from django.urls import path

from .views import create_product_view, product_detail_view, edit_product_view


urlpatterns = [
	path('add_product', create_product_view, name='add_product'),
	path('product/<str:pk>/', product_detail_view, name='product_detail'),
	path('product/<str:pk>/edit', edit_product_view, name='edit_product'), 
]
