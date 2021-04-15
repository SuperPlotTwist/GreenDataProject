from django.urls import path
from .views import UserRegisterView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")))
]