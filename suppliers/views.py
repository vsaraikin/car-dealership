from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Suppliers, SupplierPromotion
from .serializers import SuppliersSerializer, SupplierPromotionSerializer, SupplierSerializer
from rest_framework import permissions


class SuppliersViewSet(ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.AllowAny,)


class SupplierPromotionViewSet(ModelViewSet):
    queryset = SupplierPromotion.objects.all()
    serializer_class = SupplierPromotionSerializer
    permission_classes = (permissions.IsAuthenticated,)

