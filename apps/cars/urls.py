from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_cars, name='list'),
    path('<int:car_id>/order', views.order_form, name='createOrder'),
    path('<int:car_id>/', views.get_car_by_id, name='getById')
]
