from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('todos/', views.veeone, name='v1'),
]