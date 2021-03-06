from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm

from productapp.presets import ctxt_cat
from utils.errors import ERROR_MSG
from utils.views import client_error_view


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

    def get_context_data(self, *args, **kwargs):
        context = super(PasswordsChangeView,
                        self).get_context_data(*args, **kwargs)
        return ctxt_cat(context)


def PasswordSuccess(request):
    return render(request, 'registration/password_success.html')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return super(UserRegisterView, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(UserRegisterView,
                        self).get_context_data(*args, **kwargs)
        return ctxt_cat(context)


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # handle anoymous usr edition
            return client_error_view(request, ERROR_MSG['anon_profile_edit'], 403)
        else:
            return super(UserEditView, self).get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(UserEditView, self).get_context_data(*args, **kwargs)
        return ctxt_cat(context)

    def get_object(self):
        return self.request.user
