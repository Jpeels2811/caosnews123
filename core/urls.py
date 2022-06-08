from django.urls import path
from .views import main

urlpatterns = [
    path('', main,name="main"),
    path('', noticia1111, name="noticia1"),
]
