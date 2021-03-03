from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from apps.user.forms import UserRegisterForm


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user/user-card.html')
    else:
        return redirect('user:sign-in')


def sign_in(request):
    return render(request, 'user/sign-in.html')


class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('user:sign-in')
    template_name = 'user/sign-up.html'


def log_out(request):
    logout(request)
    return redirect('index')
