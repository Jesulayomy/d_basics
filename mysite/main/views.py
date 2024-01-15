from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateNewList
from .models import Item, ToDoList


# Create your views here.
def todo(response, id):
    try:
        lst = response.user.todolist.get(id=id)
    except ToDoList.DoesNotExist:
        return HttpResponse("<h2>This list does not exist or is not yours</h2>")
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
    if response.user.is_authenticated:
        todos = response.user.todolist.all()[:3]
    else:
        todos = []
    return render(response, "main/home.html", {"todos": todos})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            todo = ToDoList(name=name)
            todo.save()
            response.user.todolist.add(todo)
            return HttpResponseRedirect(f"/{todo.id}")
    else:
        form = CreateNewList()
        return render(response, "main/create.html", {"form": form})

def todos(response):
    todos = response.user.todolist.all()
    return render(response, "main/todos.html", {"todos": todos})
