from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticuloViewSet, ProveedorViewSet

router = DefaultRouter()

router.register('articulos', ArticuloViewSet, basename='articulos-api')
router.register('proveedores', ProveedorViewSet, basename='proveedores-api')


urlpatterns = [
    path('', include(router.urls)),
]
