from django.urls import path
from .views import *


urlpatterns = [
    path('', main,name="main"),
    path('PaginaRegister/',paginaregister,name="paginaregister"),
    path('PaginaLogin/', paginalogin, name="paginalogin"),
    path('formulario1/', formulario1, name="formulario1"),
    path('noticia1111/', noticia1, name="noticia1"),
    path('noticia2222/', noticia2, name="noticia2"),
    path('noticia3333/', noticia3, name="noticia3"),
    path('main logeado/', mainlogeado, name="mainlogeado"),
    path('buscador/', buscador, name="buscador"),
    path('subir noticia/', subirnoticia, name="subirnoticia"),
    path('listanoticias/', listanoticias, name="listanoticias"),
    path('form_noticia/', form_noticia, name="form_noticia"),
    path('form_mod_noticia/<codigo>', form_mod_noticia, name="form_mod_noticia"),
    path('form_del_noticia/<codigo>', form_del_noticia, name="form_del_noticia"),
   
    ]   
