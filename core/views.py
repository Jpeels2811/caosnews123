from django.shortcuts import render

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