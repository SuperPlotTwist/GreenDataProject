from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from productapp.models import Product
from productapp.urls import *
from productapp.views import *
from productapp.presets import CATEGORIES

# Create your views here.
"""def home(request):
	return render(request, 'home.html', {})"""


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    ordering = ['-barcode']

    # def get_context_data(self, *args, **kwargs):
    #     # cat_menu = Category.objects.all()
    #     # context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     # context["cat_menu"] = cat_menu
    #     return context


def AboutUsView(request):
    ctxt = {}
    return render(request, 'about_us.html', ctxt)


def list_products_view(request, cat=None):
	
    return render(request, 'list_products.html', {'categories':CATEGORIES})