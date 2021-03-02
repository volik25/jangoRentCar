from django.http import HttpResponse
from django.shortcuts import render


def start_app(request):
    return render(request, 'main/main.html')
