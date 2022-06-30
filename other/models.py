from django.db import models


class InstanceStatus(models.Model):
    """ An abstract model that show the status of instances """
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True, verbose_name='Time created')
    edited = models.DateTimeField(auto_now=True, verbose_name='Time edited')

    class Meta:
        abstract = True


class PromotionsAndDiscounts(models.Model):
    """ An abstract model that store promotions and discounts """
    discount = models.DecimalField(default=0, max_digits=10, verbose_name="Buyer's discount", decimal_places=2)

    class Meta:
        abstract = True


def get_chars():
    characteristics_car = {
        'car_brand': [],
        'car_model': [],
        'engine_type': [],
        'transmission': [],
        'color': []
    }
    return characteristics_car
