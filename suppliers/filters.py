from django_filters import rest_framework as filters
from .models import Suppliers


class SuppliersFilter(filters.Filter):
    class Meta:
        model = Suppliers
        fields = '__all__'
