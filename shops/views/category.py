from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shops.models import Category
from shops.serializers import (CategorySerializer, CategoryCreateSerializer)
from shops.service import PaginationCategory


class CatViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = PaginationCategory

    def get_serializer_class(self):
        serializer_class = CategorySerializer

        if self.action == 'create':
            serializer_class = CategoryCreateSerializer
        return serializer_class
