from django.shortcuts import render
from django.views import View
from .forms import CustomUserLoginForm


class LoginView(View):
    def get(self, request):
        form = CustomUserLoginForm
        return render(request, 'user/login.html', {'form': form})
