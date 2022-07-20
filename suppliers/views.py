from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Suppliers, SupplierPromotion
from .serializers import SuppliersSerializer, SupplierPromotionSerializer, SupplierSerializer
from rest_framework import permissions


class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = (permissions.AllowAny,)


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.AllowAny,)


class SupplierPromotionViewSet(ModelViewSet):
    queryset = SupplierPromotion.objects.all()
    serializer_class = SupplierPromotionSerializer
    permission_classes = (permissions.IsAuthenticated,)

