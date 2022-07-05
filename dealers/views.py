from rest_framework.viewsets import ModelViewSet
from .models import Dealer, Dealers, DealerPromotion, DealerToBuyer, SupplierToDealer
from .serializers import DealerSerializer, DealersSerializer, DealerPromotionSerializer, DealerToBuyerSerializer, \
    SupplierToDealerSerializer


class DealersViewSet(ModelViewSet):
    queryset = Dealers.objects.all()
    serializer_class = DealersSerializer


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerPromotionViewSet(ModelViewSet):
    queryset = DealerPromotion.objects.all()
    serializer_class = DealerPromotionSerializer


class DealerToBuyerViewSet(ModelViewSet):
    queryset = DealerToBuyer.objects.all()
    serializer_class = DealerToBuyerSerializer


class SupplierToDealerViewSet(ModelViewSet):
    queryset = SupplierToDealer.objects.all()
    serializer_class = SupplierToDealerSerializer


from django.http import HttpResponse, HttpResponseNotFound
def index(request):
    return HttpResponse("hello")

