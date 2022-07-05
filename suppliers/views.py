from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Suppliers, SupplierPromotion
from .serializers import SuppliersSerializer, SupplierPromotionSerializer, SupplierSerializer


class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierPromotionViewSet(ModelViewSet):
    queryset = SupplierPromotion.objects.all()
    serializer_class = SupplierPromotionSerializer
