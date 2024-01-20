from typing import Any
from django.contrib.auth.models import User
from mysite.celery import app

from .models import ToDoList, Item
from main.signals import create_daily_list


@app.task
def create_daily():
    users = User.objects.all()
    for user in users:
        create_daily_list(user)


@app.task
def daily_reset():
    daily_lists = ToDoList.objects.filter(is_daily=True)
    for daily_list in daily_lists:
        for item in daily_list.item_set.all():
            item.complete = False
            item.save()

    print('Daily ToDoList reset successfully')
