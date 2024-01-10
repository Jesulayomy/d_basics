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
    if response.method == "POST":
        if response.POST.get("save"):
            for item in lst.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                lst.item_set.create(text=txt, complete=False)

    return render(response,"main/todo.html", {"todo": lst})

def home(response):
    todos = ToDoList.objects.all()
    return render(response, "main/home.html", {"todos": todos})

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

def todos(response):
    todos = ToDoList.objects.all()
    return render(response, "main/todos.html", {"todos": todos})