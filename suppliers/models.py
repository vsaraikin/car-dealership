from django.db import models
from djmoney.models.fields import MoneyField
from other.models import InstanceStatus, PromotionsAndDiscounts


class Suppliers(InstanceStatus):
    """ Model for Suppliers network"""
    name = models.CharField(verbose_name="Supplier's name", max_length=20)
    founded_year = models.DateTimeField(verbose_name="Foundation year")
    buyers_amount = models.PositiveIntegerField(verbose_name="Buyers amount")
    car_list = models.PositiveIntegerField(verbose_name="Car for sale")

    class Meta:
        verbose_name_plural = "Suppliers"

    def __str__(self):
        return f'{self.name}'


class Supplier(InstanceStatus):
    """ Model for a one particular Supplier"""
    price = MoneyField(verbose_name="Supplier's price", max_length=2, default_currency="USD", max_digits=10)
    car = models.ForeignKey('cars.Car', on_delete=models.SET_NULL, null=True)
    name = models.ForeignKey('suppliers.Suppliers', verbose_name="Name", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Supplier"

    def __str__(self):
        return f'{self.car} for {self.price}'


class SupplierPromotion(PromotionsAndDiscounts):
    """ A model to create promotions for Supplier """
    supplier = models.ForeignKey(Suppliers, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.supplier} sells the {self.car} with {self.discount}% discount!"
