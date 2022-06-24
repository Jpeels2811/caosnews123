from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Noticia
from .serializers import NoticiaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_noticias(request):
    if request.method == 'GET':
        lista = Noticia.objects.all()
        serializer = NoticiaSerializer(lista, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_noticia(request,id):
    try:
        noticia = Noticia.objects.get(codigo=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = NoticiaSerializer(noticia)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoticiaSerializer(noticia, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Noticia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)