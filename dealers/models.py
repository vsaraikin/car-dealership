from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from other.models import InstanceStatus, PromotionsAndDiscounts, get_chars


class Dealers(InstanceStatus):
    """ Model for dealership network """
    name = models.CharField(max_length=200, verbose_name="Dealer's name")
    location = CountryField(verbose_name="Dealer's location")
    balance = MoneyField(verbose_name="Dealer's balance", default_currency="USD", max_digits=10)
    characteristics_of_car = models.JSONField(default=get_chars)

    def __str__(self):
        return f"{self.name} - {self.location}"

    class Meta:
        verbose_name_plural = "Dealers"


class Dealer(InstanceStatus):
    """ Model for a one particular dealer """
    dealer = models.ForeignKey(Dealers, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey("suppliers.Supplier", on_delete=models.SET_NULL, null=True)
    car_count = models.PositiveIntegerField(default=0, verbose_name='Car counter')
    price = MoneyField(decimal_places=2, verbose_name="Dealer's price", default_currency="USD", max_digits=10)

    def __str__(self):
        return f"{self.dealer} - {self.car}"

    class Meta:
        verbose_name_plural = "Dealer"


class DealerToBuyer(InstanceStatus):
    """ Model to store transaction from Dealer to Buyer """
    car = models.ForeignKey('dealers.Dealer', on_delete=models.SET_NULL, null=True)
    dealer = models.ForeignKey('dealers.Dealers', on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey('buyers.Buyers', on_delete=models.SET_NULL, null=True)
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    car_count = models.PositiveIntegerField(default=1)
    total_sum = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='Total sum',
                           default=0)

    def __str__(self):
        return f'{self.car} : from {self.dealer} to {self.buyer}'

    class Meta:
        verbose_name_plural = "Dealer to Buyer transactions"


class SupplierToDealer(InstanceStatus):
    """ Model to store transaction from Supplier to Dealer """
    car = models.ForeignKey("suppliers.Supplier", on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey('suppliers.Suppliers', on_delete=models.SET_NULL, verbose_name='Supplier', null=True)
    dealer = models.ForeignKey(Dealers, on_delete=models.SET_NULL, verbose_name='Buyer', null=True)
    price = MoneyField(decimal_places=2, default_currency='USD', max_digits=10)
    car_count = models.PositiveIntegerField(default=1)
    total_cost = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='Total cost', default=0)

    def __str__(self):
        return f'{self.car} : from {self.supplier} to {self.dealer}'

    class Meta:
        verbose_name_plural = "Supplier to Dealer transactions"


class DealerPromotion(PromotionsAndDiscounts):
    """ A model for creating promotions """
    dealership = models.ForeignKey(Dealers, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.dealership} has {self.discount}% discount on {self.car} "


class DealerStatistic(models.Model):
    """ A model for Dealer's statistics """
    dealer_stats = models.ForeignKey(Dealers, on_delete=models.SET_NULL, null=True)
    cost = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    revenue = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD')
    total_bought_car_count = models.PositiveIntegerField(default=0)
    total_sold_car_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.dealer_stats} - {self.revenue} - {self.cost}"
