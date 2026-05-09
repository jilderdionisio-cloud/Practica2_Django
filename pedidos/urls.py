from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, PedidoViewSet


router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
