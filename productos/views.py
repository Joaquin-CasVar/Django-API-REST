from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Articulo, Proveedor
from .serializers import ArticuloSerializer, ProveedorSerializer, ArticuloPublicSerializer

@api_view(['GET', 'POST'])
def articulos(request):
    if request.method == 'GET':
        articulos = Articulo.objects.all().select_related('proveedor')
        serializer = ArticuloPublicSerializer(articulos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ArticuloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Articulo creado'}, status=status.HTTP_201_CREATED)

        return Response({'mensaje': 'Datos invalidos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def articulos_detail(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)

    if request.method == 'GET':
        serializer = ArticuloSerializer(articulo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ArticuloSerializer(articulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Articulo actualizado'}, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Datos invalidos'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        articulo.delete()
        return Response({'mensaje': 'Articulo eliminado'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def proveedores(request):
    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        serializer = ProveedorSerializer(proveedor, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Proveedor creado'}, status=status.HTTP_201_CREATED)

        return Response({'mensaje': 'Datos invalidos'}, status=status.HTTP_400_BAD_REQUEST)

