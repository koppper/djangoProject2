from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shops.models import Shop
from shops.serializers import ShopSerializer
from shops.service import PaginationShop


class ShopViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    pagination_class = PaginationShop