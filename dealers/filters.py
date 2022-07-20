from django_filters import rest_framework as filters
from .models import Dealers, Dealer


class DealersFilter(filters.Filter):
    class Meta:
        model = Dealers
        fields = '__all__'


class DealerFilter(filters.Filter):
    class Meta:
        model = Dealer
        fields = '__all__'
