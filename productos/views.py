from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Articulo, Proveedor
from .serializers import ArticuloSerializer, ArticuloPublicSerializer, ProveedorSerializer

class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all().select_related('proveedor')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = {
        'proveedor': ['exact'], 
        'precio': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'proveedor__activo': ['exact'],
    }
    search_fields = ['nombre', 'proveedor__nombre']
    ordering_fields = ['precio', 'id', 'nombre']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticuloPublicSerializer
        else:
            return ArticuloSerializer

#   Ejemplo de borrado logico (para implementar en consesionaria)

    # @action(detail=True, methods=['delete'])
    # def logico(self, request, pk=None):
    #     articulo = self.get_object()
    #     articulo.activo = False
    #     articulo.save()
    #     return Response({'status': 'Articulo eliminado (logico)'})


class ProveedorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProveedorSerializer
