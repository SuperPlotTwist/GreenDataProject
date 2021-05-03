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
    ordering = ['-last_modified']

    # def get_context_data(self, *args, **kwargs):
    #     # cat_menu = Category.objects.all()
    #     # context = super(HomeView, self).get_context_data(*args, **kwargs)
    #     # context["cat_menu"] = cat_menu
    #     return context


def AboutUsView(request):
    ctxt = {}
    return render(request, 'about_us.html', ctxt)


def list_products_view(request, cat=None):
    """
    Query the database and display all products in category cat
    """
    ctxt = {'good_cat': True}
    
    # if the category given exists, query all products in this category
    if any(cat in c for c in CATEGORIES):
        items = Product.objects.filter(category=cat)
        ctxt['products'] = items
        ctxt['category'] = cat
    else:
        ctxt['good_cat'] = False

    return render(request, 'list_products.html', ctxt)