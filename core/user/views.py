from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'


    def get_success_url(self):
        return reverse_lazy('profiles')
