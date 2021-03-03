from django.http import HttpResponse, Http404
from django.shortcuts import render

from apps.cars.models import Car


def get_cars(request):
    car_list = Car.objects.order_by('manufacturer')
    return render(request, 'cars/car-list.html', {'car_list': car_list})


def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404('Такого автомобиля не существует')

    return render(request, 'cars/car.html', {'car': car})


def order_form(request, car_id):
    return render(request, 'cars/order.html', {'car_id': car_id})


def create_order(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404('Такого автомобиля не существует')

    return render(request)

