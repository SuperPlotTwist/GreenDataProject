"""GreenData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import HomeView, AboutUsView, list_products_view, searchView, allProductsView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


urlpatterns = [
    #path('', views.home, name="home")
    path('allproducts/', allProductsView.as_view(), name="allproducts"),
    path('aboutus/', AboutUsView, name='aboutus'),
	path('category/<str:cat>', list_products_view, name='category'),
    path('', HomeView, name='home'),
	path('category/', list_products_view, name='category'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('search', searchView, name='search-results'),
]