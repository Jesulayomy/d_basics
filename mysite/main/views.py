from django.http import HttpResponse
from django.shortcuts import render

from .models import Item, ToDoList

# Create your views here.
def index(response, id):
    try:
        lst = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("<h1>This list does not exist</h1>")

    tsk = lst.item_set.all()
    output = "<h1>" + lst.name + "</h1>"
    for item in tsk:
        status = "Completed" if item.complete else "Not Completed"
        output += "<li>" + item.text + " - " + status + "</li>"
    return HttpResponse(output)

def veeone(response):
    return HttpResponse("<h1>Hello V1</h1>")
