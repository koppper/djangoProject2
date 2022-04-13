from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shops.views import GoodsViewSet, ShopViewSet, CatViewSet

router = DefaultRouter()
router.register('goods', GoodsViewSet)
router.register('shops', ShopViewSet)
router.register('cat', CatViewSet)

urlpatterns = [
] + router.urls
