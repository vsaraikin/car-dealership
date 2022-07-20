from rest_framework.viewsets import ModelViewSet
from .models import Buyers, BuyerHistory, BuyerOffer
from .serializers import BuyersSerializer, BuyerHistorySerializer, BuyerOfferSerializer
from rest_framework import permissions


class BuyersViewSet(ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer
    permission_classes = (permissions.AllowAny,)


class BuyerHistoryViewSet(ModelViewSet):
    queryset = BuyerHistory.objects.all()
    serializer_class = BuyerHistorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class BuyerOfferViewSet(ModelViewSet):
    queryset = BuyerOffer.objects.all()
    serializer_class = BuyerOfferSerializer
    permission_classes = (permissions.IsAuthenticated,)
