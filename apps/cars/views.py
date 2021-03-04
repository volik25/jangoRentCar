from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from apps.cars.forms import OrderForm
from apps.cars.models import Car, Order


def get_cars(request):
    car_list = Car.objects.order_by('manufacturer')
    return render(request, 'cars/car-list.html', {'car_list': car_list})


def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except:
        raise Http404('Такого автомобиля не существует')

    return render(request, 'cars/car.html', {'car': car})


def create_order(request, car_id):
    is_error = False
    error_text = ''
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            try:
                order = order_form.save(commit=False)
                order.user = request.user
                car = Car.objects.get(id=car_id)
                order.car = car
                order.save()
                order_id = Order.objects.latest('id').id
                return redirect('cars:order', order_id=order_id)
            except:
                is_error = True
                error_text = 'Ошибка создания заявки'
        else:
            is_error = True
            error_text = 'Некорректно заполнена форма'
    order_form = OrderForm()
    data = {
        'form': order_form,
        'error': is_error,
        'error_text': error_text
    }
    return render(request, 'cars/order-form.html', data)


def get_order_by_id(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'cars/order.html', {'order': order})
