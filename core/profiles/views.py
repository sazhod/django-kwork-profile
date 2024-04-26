from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user = request.user
        user_group = user.groups.first()
        print(request.user.groups.first())
        print(request.user.is_authenticated)

        # TODO: user_group not equal Client and Executor
        if user.groups.first() == 'Client':
            return render(request, 'profiles/client_profile.html')
        elif user.groups.first() == 'Executor':
            return render(request, 'profiles/executor_profile.html')
