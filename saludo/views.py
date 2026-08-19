from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def saludo(request):
    return Response({'Hola': 'mundo'}, status=status.HTTP_200_OK)
