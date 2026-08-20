from rest_framework import serializers
from .models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [
            'id',
            'nombre',
            'precio',
            'stock',
            'timestamp',
        ]
        read_only_fields = ['id', 'timestamp']
