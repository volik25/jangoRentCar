from django.urls import path

from cars4rent.apps.cars import index

urlpatterns = [
    path('', index)
]
