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

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class ProductDetailView(DetailView):
	model = Product
	template_name = 'product_detail.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all() 
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddProductView(CreateView):
	model = Product
	form_class = AddForm
	template_name = 'add_product.html'
	#fields = '__all__'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddProductView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class UpdateProductView(UpdateView):
	model = Product
	form_class = AddForm
	template_name = 'update_product.html'
	#fields = ['product_name', 'packaging', 'packaging_mass', 'author']
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(UpdateProductView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


class DeleteProductView(DeleteView):
	model = Product
	template_name = 'delete_product.html'
	success_url = reverse_lazy('home')
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeleteProductView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddCategoryView(CreateView):
	model = Category
	template_name = 'add_category.html'
	fields = '__all__'
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def AboutUsView(request):
	ctxt = {}
	return render(request, 'about_us.html', ctxt)

'''
def CategoryView(request, cats, **kwargs):
	ctxt = {}

	cat_menu = Category.objects.all()
	cat_products = Product.objects.filter(category=cats.replace('-', ' '))
	
	ctxt["cat_menu"] = cat_menu
	ctxt["cat_products"] = cat_products
	ctxt["cats"] = cats.title().replace('-', ' ')

	return render(request, 'categories.html', ctxt)'''