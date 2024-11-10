from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query<text>', views.querybutton, name='querybutton'),
    path('command<text>', views.commandbutton, name='commandbutton'),
]
