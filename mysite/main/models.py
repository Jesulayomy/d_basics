from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    """ A list of tasks to do """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)
    is_daily = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def incomplete(self):
        counter = 0
        for item in self.item_set.all():
            if not item.complete:
                counter += 1
        return counter


class Item(models.Model):
    """ A task on a specific list """
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
