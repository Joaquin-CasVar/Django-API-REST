from django.urls import path

from .views import ArticuloListCreateAPIView, ArticulosDetailAPIView, proveedores

urlpatterns = [
    path('articulos/', ArticuloListCreateAPIView.as_view(), name='articulos_api'),
    path('articulos/<int:pk>/', ArticulosDetailAPIView.as_view(), name='articulo_detail_api'),
    path('proveedores/', proveedores, name='proveedores_api'),
]
