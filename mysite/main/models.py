from django.db import models

# Create your models here.
class ToDoList(models.Model):
    """ A list of tasks to do """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    """ A task on a specific list """
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
