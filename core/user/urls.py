from django.contrib import admin
from django.urls import path
from .views import LoginUserView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    # TODO: logout/ - Page not found
    path('logout/', LogoutView.as_view(), name='logout')
]
