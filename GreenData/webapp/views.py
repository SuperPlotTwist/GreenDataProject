from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from productapp.models import Product
from productapp.urls import *
from productapp.views import *
from productapp.presets import CATEGORIES
from productapp.presets import ctxt_cat


def searchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        prod = Product.objects.filter(name__contains=searched)
        return render(request, 'search.html',
                      ctxt_cat({
                          'searched': searched,
                          'prod': prod
                      }))
    else:
        last_ten = Product.objects.all().order_by('last_modified')[:10]
        prod = reversed(last_ten)
        return render(request, 'search.html', ctxt_cat({'prod': prod}))


def HomeView(request):
    ctxt = {}
    last_ten = Product.objects.all().order_by('-last_modified')[:10]
    ctxt["products"] = last_ten
    ctxt['products_empty'] = len(last_ten) == 0
    return render(request, 'home.html', ctxt_cat(ctxt))


class allProductsView(ListView):
    model = Product
    template_name = 'all_products.html'
    ordering = ['-last_modified']

    def get_context_data(self, *args, **kwargs):
        context = super(allProductsView,
                        self).get_context_data(*args, **kwargs)
        return ctxt_cat(context)


def AboutUsView(request):
    context = {}
    return render(request, 'about_us.html', ctxt_cat(context))


def list_products_view(request, cat=None):
    """
    Query the database and display all products in category cat
    """
    ctxt = {'good_cat': True}
    ctxt = ctxt_cat(ctxt)
    # if the category given exists, query all products in this category
    if any(cat in c for c in CATEGORIES):
        items = Product.objects.filter(category=cat)
        ctxt['products'] = items
        ctxt['category'] = cat
    else:
        ctxt['good_cat'] = False

    return render(request, 'list_products.html', ctxt)