from rest_framework.viewsets import ModelViewSet
from .models import Buyers, BuyerHistory, BuyerOffer
from .serializers import BuyersSerializer, BuyerHistorySerializer, BuyerOfferSerializer


class BuyersViewSet(ModelViewSet):
    queryset = Buyers.objects.all()
    serializer_class = BuyersSerializer


class BuyerHistoryViewSet(ModelViewSet):
    queryset = BuyerHistory.objects.all()
    serializer_class = BuyerHistorySerializer


class BuyerOfferViewSet(ModelViewSet):
    queryset = BuyerOffer.objects.all()
    serializer_class = BuyerOfferSerializer
