from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request handler
# Requests and response

def calculate():
    x = 1
    y = 2
    return x


def say_hola(request):
    """ Recieves a request and sends a response """
    x = calculate()
    return render(request, 'hello.html', {'name': 'Layomi'})
