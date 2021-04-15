from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import AddForm

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
	form_class = AddForm
	template_name = 'add_product.html'
	#fields = '__all__'

class UpdateProductView(UpdateView):
	model = Product
	form_class = AddForm
	template_name = 'update_product.html'
	#fields = ['product_name', 'packaging', 'packaging_mass', 'author']

	