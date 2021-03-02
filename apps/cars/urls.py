from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_cars, name='list'),
    path('<int:car_id>/', views.get_car_by_id, name='getById')
]
