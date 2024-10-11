from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для просмотра продуктов.

    Методы:
    - list: Возвращает список всех продуктов.
    - retrieve: Возвращает детали определенного продукта.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
