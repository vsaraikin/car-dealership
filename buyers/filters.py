from django_filters import rest_framework as filters
from .models import Buyers, BuyerHistory


class BuyersFilter(filters.Filter):
    class Meta:
        model = Buyers
        fields = '__all__'


class BuyerHistoryFilter(filters.Filter):
    class Meta:
        model = BuyerHistory
        fields = '__all__'
