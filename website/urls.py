from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.querybutton, name='querybutton'),
    path('command/', views.commandbutton, name='commandbutton'),
]
