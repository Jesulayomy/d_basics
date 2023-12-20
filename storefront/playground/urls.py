from django.urls import path
from . import views

# url configurations
urlpatterns = [
    path('hello/', views.say_hola),
]