from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .forms import AddForm
from django.urls import reverse_lazy

# Create your views here.
"""def home(request):
	return render(request, 'home.html', {})"""

class HomeView(ListView):
	model = Product
	template_name = 'home.html'
	ordering = ['-id']

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

class DeleteProductView(DeleteView):
	model = Product
	template_name = 'delete_product.html'
	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'

def CategoryView(request, cats):
	cat_products = Product.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'cat_products':cat_products})