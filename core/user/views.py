from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserLoginForm


class LoginUserView(LoginView):
    form_class = CustomUserLoginForm
    template_name = 'user/login.html'

