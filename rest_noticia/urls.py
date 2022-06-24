from django.urls import path
from .views import lista_noticias, detalle_noticia
from rest_noticia.viewslogin import login

urlpatterns = [
    path('lista_noticias',lista_noticias,name="lista_noticias"),
    path('detalle_noticia/<id>',detalle_noticia,name="detalle_noticia"),
    path('login',login,name="login"),
]