from rest_framework import serializers
from .models import Suppliers, Supplier, SupplierPromotion


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ["id", "name", "founded_year", "buyers_amount", "car_list"]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'price', 'car', 'name']


class SupplierPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierPromotion
        fields = ['id', 'supplier', 'car']
