from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Dealer, Dealers, DealerPromotion, DealerToBuyer, SupplierToDealer
from .serializers import DealerSerializer, DealersSerializer, DealerPromotionSerializer, DealerToBuyerSerializer, \
    SupplierToDealerSerializer


class DealersViewSet(ModelViewSet):
    queryset = Dealers.objects.all()
    serializer_class = DealersSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'location', 'balance']
    search_fields = ['id', 'name', 'location', 'balance']
    ordering_fields = ['id', 'name', 'location', 'balance']


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class DealerPromotionViewSet(ModelViewSet):
    queryset = DealerPromotion.objects.all()
    serializer_class = DealerPromotionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class DealerToBuyerViewSet(ModelViewSet):
    queryset = DealerToBuyer.objects.all()
    serializer_class = DealerToBuyerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class SupplierToDealerViewSet(ModelViewSet):
    queryset = SupplierToDealer.objects.all()
    serializer_class = SupplierToDealerSerializer
    permission_classes = (permissions.IsAuthenticated,)


from django.http import HttpResponse


def index(request):
    return HttpResponse("hello")
