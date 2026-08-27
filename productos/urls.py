from django.urls import path

from .views import articulos, articulos_detail, proveedores

urlpatterns = [
    path('articulos/', articulos, name='articulos_api'),
    path('articulos/<int:pk>/', articulos_detail, name='articulo_detail_api'),
    path('proveedores/', proveedores, name='proveedores_api'),
]
