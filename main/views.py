from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader


def main_page(request):
    template = loader.get_template('main/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

