from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins

from .models import Articulo, Proveedor
from .serializers import ArticuloSerializer, ProveedorSerializer, ArticuloPublicSerializer

# clase APIView

# clase Generics APIView

# clase Concrete Generics APIView

class ArticuloListCreateAPIView(generics.ListCreateAPIView):
    queryset = Articulo.objects.all().select_related('proveedor')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticuloPublicSerializer
        else:
            return ArticuloSerializer


# class ArticulosGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Articulo.objects.all().select_related('proveedor')

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return ArticuloPublicSerializer
#         else:
#             return ArticuloSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class ArticulosAPIView(APIView):
#     def get(self, request):
#         articulos = Articulo.objects.all().select_related('proveedor')
#         serializer = ArticuloPublicSerializer(articulos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ArticuloSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {'mensaje': 'Articulo creado'}, 
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )

class ArticulosDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer


# class ArticulosDetailGenericAPIView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Articulo.objects.all()
#     serializer_class = ArticuloSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class ArticulosDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Articulo, pk=pk)

#     def get(self, request, pk):
#         articulo = self.get_object(pk)

#         serializer = ArticuloSerializer(articulo)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         articulo = self.get_object(pk)

#         serializer = ArticuloSerializer(articulo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {'mensaje': 'Articulo actualizado'}, 
#                 status=status.HTTP_200_OK
#             )
#         return Response(
#             serializer.errors, 
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, pk):
#         articulo = self.get_object(pk)

#         articulo.delete()
#         return Response(
#             {'mensaje': 'Articulo eliminado'}, 
#             status=status.HTTP_200_OK
#         )




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

