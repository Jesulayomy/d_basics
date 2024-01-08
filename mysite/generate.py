from main.models import ToDoList, Item


def run_generate():
    t = ToDoList(name="Groceries")
    t.save()

    t = ToDoList(name="Homework")
    t.save()

    item = t.item_set.create(text="Buy milk", complete=False)
    item.save()
