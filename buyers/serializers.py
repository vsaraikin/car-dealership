from rest_framework import serializers
from .models import Buyers, BuyerHistory, BuyerOffer


class BuyersSerializer(serializers.ModelSerializer):
    """ Buyer Serializer """
    class Meta:
        model = Buyers
        fields = ["id", "first_name", "last_name", "balance"]


class BuyerHistorySerializer(serializers.ModelSerializer):
    """ Buyer History serializer """
    class Meta:
        model = BuyerHistory
        fields = ["id", "buyer", "car", "price", "date_bought"]


class BuyerOfferSerializer(serializers.ModelSerializer):
    """ Buyer Offer Serializer """
    class Meta:
        model = BuyerOffer
        fields = ["id", "buyer", "max_price", "characteristics_of_car"]
