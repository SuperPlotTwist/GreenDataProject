from django.urls import path
from .views import UserRegisterView, UserEditView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_view.PasswordChangeView.as_view(template_name='registration/change_password.html'))
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")))
]