from rest_framework import serializers
from .models import Dealers, Dealer, DealerToBuyer, DealerPromotion, SupplierToDealer


class DealersSerializer(serializers.ModelSerializer):
    """ Dealers' network serializer """
    class Meta:
        model = Dealers
        fields = ['id', 'name', 'location', 'balance', 'characteristics_of_car']


class DealerSerializer(serializers.ModelSerializer):
    """ Dealer's serializer"""
    class Meta:
        model = Dealer
        fields = ['id', 'car', 'dealer', 'car_count', 'price']


class DealerToBuyerSerializer(serializers.ModelSerializer):
    """ Dealer to Buyer history serializer """
    class Meta:
        model = DealerToBuyer
        fields = ['id', 'car', 'dealer', 'buyer', 'price']


class SupplierToDealerSerializer(serializers.ModelSerializer):
    """ Supplier to Dealer history serializer """
    class Meta:
        model = SupplierToDealer
        fields = ['car', 'supplier', 'dealer', 'price', 'car_count']


class DealerPromotionSerializer(serializers.ModelSerializer):
    """ Dealer promotion serializer """
    class Meta:
        model = DealerPromotion
        fields = ['id', 'dealership', 'car']
