from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Buyers, BuyerHistory, BuyerOffer
from .serializers import BuyersSerializer, BuyerHistorySerializer, BuyerOfferSerializer
from rest_framework import permissions


class BuyersViewSet(ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class BuyerHistoryViewSet(ModelViewSet):
    queryset = BuyerHistory.objects.all()
    serializer_class = BuyerHistorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'


class BuyerOfferViewSet(ModelViewSet):
    queryset = BuyerOffer.objects.all()
    serializer_class = BuyerOfferSerializer
    permission_classes = (permissions.IsAuthenticated,)
