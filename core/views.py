from django.shortcuts import render, redirect
from .models import Noticia
from .forms import NoticiaForm

# Create your views here.

def main(request):
    return render(request,'core/main.html')

def buscador(request):
    return render(request,'core/buscador.html')

def formulario1(request):
    return render(request,'core/formulario1.html')

def mainlogeado(request):
    return render(request,'core/main logeado.html')

def noticia1(request):
    return render(request,'core/noticia1111.html')

def noticia2(request):
    return render(request,'core/noticia2222.html')

def noticia3(request):
    return render(request,'core/noticia3333.html')

def paginalogin(request):
    return render(request,'core/PaginaLogin.html')

def paginaregister(request):
    return render(request,'core/PaginaRegister.html')

def subirnoticia(request):
    return render(request,'core/subir noticia.html')


def listanoticias(request):

    noticias= Noticia.objects.all()

    datos ={
        'noticias' : noticias
    }
    return render(request, 'core/listanoticias.html', datos)


def form_noticia(request):

    datos ={
        'form' : NoticiaForm()
    }
    if request.method=='POST':
        formulario=NoticiaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos guardados correctamente'
    return render(request, 'core/form_noticia.html', datos)

def form_mod_noticia(request, codigo):
    noticia = Noticia.objects.get(codigo=codigo)
    datos = { 
        'form': NoticiaForm(instance=noticia),
        }
    if request.method=='POST':
        formulario=NoticiaForm(data=request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje']='Datos modificados correctamente'
    return render(request, 'core/form_mod_noticia.html', datos)

def form_del_noticia( request, codigo):
    noticia = Noticia.objects.get(codigo=codigo)
    noticia.delete()
    return redirect(to="mainlogeado")