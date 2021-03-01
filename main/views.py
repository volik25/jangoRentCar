from django.http import HttpResponse


def start_app(request):
    return HttpResponse('Главная')
