from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello Layo and Tim</h1>")

def veeone(response):
    return HttpResponse("<h1>Hello V1</h1>")
