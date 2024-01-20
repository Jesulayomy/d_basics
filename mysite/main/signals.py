from .models import ToDoList


def create_daily_list(user):
    daily_list, created = ToDoList.objects.get_or_create(
        user=user,
        name=f'{user.username}\'s Daily',
        is_daily=True
    )
