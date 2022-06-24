from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import *

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['codigo','titulo','fecha','ubicacion','descripcion','categoria']




        