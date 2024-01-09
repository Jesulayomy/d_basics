from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList
from .models import Item, ToDoList


# Create your views here.
def todo(response, id):
    try:
        lst = ToDoList.objects.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("<h1>This list does not exist</h1>")

    return render(response,"main/todo.html", {"todo": lst})

def home(response):
    return render(response,"main/home.html", {"name": "Home Page"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todo = ToDoList(name=name)
            todo.save()
            return HttpResponseRedirect(f"/{todo.id}")
    else:
        form = CreateNewList()
        return render(response, "main/create.html", {"form": form})
