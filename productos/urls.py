from django.urls import path

from .views import articulos, articulos_detail

urlpatterns = [
    path('', articulos, name='articulos_api'),
    path('<int:pk>/', articulos_detail, name='articulo_detail_api')
]
