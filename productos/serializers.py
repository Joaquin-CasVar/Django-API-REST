from rest_framework import serializers
from .models import Articulo, Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [
            'id',
            'nombre',
            'precio',
            'stock',
            'proveedor', #pk
            'timestamp',
        ]
        read_only_fields = ['id', 'timestamp']


class ArticuloPublicSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = [
            'id',
            'nombre',
            'precio',
            'proveedor', # nested field
        ]
        read_only_fields = ['id', 'timestamp']
