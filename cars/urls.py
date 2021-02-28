from django.urls import path

from cars.views import index

urlpatterns = [
    path('', index)
]
