from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from productapp.models import Product
from productapp.urls import *
from productapp.views import *

# Create your views here.
"""def home(request):
	return render(request, 'home.html', {})"""

def searchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        prod = Product.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'prod':prod})
    else:
        last_ten = Messages.objects.filter(since=since).order_by('-id')[:10]
        prod = reversed(last_ten)
        return render(request, 'search.html', {'prod':prod})


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
