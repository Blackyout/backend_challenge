from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connection
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters

from .models import Person, Product
from .serializers import PersonSerializer, ProductSerializer

# Filtros personalizados para rango de precios
class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['sku', 'price_min', 'price_max']

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['email', 'last_name']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name'] # Búsqueda parámetro 'q' se mapea a 'search' en DRF por defecto
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

# Health Checks
@api_view(['GET'])
def healthz(request):
    """Liveness probe: App is running"""
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def readyz(request):
    """Readiness probe: Database is connected"""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return Response({"status": "ready", "db": "connected"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"status": "not ready", "error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)