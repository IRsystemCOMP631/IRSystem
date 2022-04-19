from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")

def homepage(request):
    context          = {}
    context['hello'] = 'Hello World'
    return render(request, 'homepage.html', context)
