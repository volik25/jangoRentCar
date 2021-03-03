from django.contrib.auth import logout
from django.shortcuts import render, redirect


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user/user-card.html')
    else:
        return redirect('user:sign-in')


def sign_in(request):
    return render(request, 'user/sign-in.html')


def sign_up(request):
    return render(request, 'user/sign-up.html')


def log_out(request):
    logout(request)
    return redirect('index')
