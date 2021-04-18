from django.urls import path

from .views import create_product_view, product_detail_view


urlpatterns = [
	path('create', create_product_view, name='create'),
	path('product/<str:pk>/', product_detail_view, name='detail')
]
