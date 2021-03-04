from django.http import HttpResponse
from django.shortcuts import render

from apps.cars.models import Order


def start_app(request):
    orders = Order.objects.order_by('createDate')[:5]
    return render(request, 'main/main.html', {'order_list': orders})
