from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Product

# Create your views here.
"""def home(request):
	return render(request, 'home.html', {})"""

class HomeView(ListView):
	model = Product
	template_name = 'home.html'

class ProductDetailView(DetailView):
	model = Product
	template_name = 'product_detail.html'

class AddProductView(CreateView):
	model = Product
	template_name = 'add_product.html'
	fields = '__all__'
