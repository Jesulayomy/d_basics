from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('v1/', views.veeone, name='v1'),
]