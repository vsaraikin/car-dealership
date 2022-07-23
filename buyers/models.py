from django.db import modelsfrom djmoney.models.fields import MoneyFieldfrom other.models import InstanceStatus, get_charsclass Buyers(InstanceStatus):    """ Model for all the Buyers """    first_name = models.CharField(verbose_name="First name", max_length=30)    last_name = models.CharField(verbose_name="Last name", max_length=30)    balance = MoneyField(verbose_name="Buyer's balance", default_currency="USD", decimal_places=2, max_digits=10)    characteristics_of_car = models.JSONField(default=get_chars, verbose_name="Preferred Characteristics")    class Meta:        verbose_name_plural = "Buyers"    def __str__(self):        return f'{self.first_name} {self.last_name}'class BuyerHistory(InstanceStatus):    """ Model for a History of a one particular Buyer"""    buyer = models.ForeignKey(Buyers, verbose_name="Buyer's name", on_delete=models.SET_NULL, null=True)    car = models.ForeignKey('dealers.Dealer', verbose_name="Car bought", on_delete=models.SET_NULL, null=True)    price = MoneyField(verbose_name="Price", max_digits=10, default_currency="USD", decimal_places=2)    date_bought = models.DateField(verbose_name="Date of purchase", auto_now_add=True)    class Meta:        verbose_name_plural = "History of Buyer's purchases"    def __str__(self):        return f'{self.buyer} - {self.car}'class BuyerOffer(InstanceStatus):    """ Offer that Buyer would like to accept """    buyer = models.ForeignKey(Buyers, verbose_name='Buyer', on_delete=models.SET_NULL, null=True)    max_price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='USD', verbose_name='Max price')    characteristics_of_car = models.JSONField(default=get_chars, verbose_name="Preferred Characteristics")    active_status = models.BooleanField(default=True, verbose_name='Offer status')    def __str__(self):        return f'{self.buyer} Offer'