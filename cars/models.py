from django.db import models
from other.models import InstanceStatus
from .car_types import ENGINE_CHOICES, COLOR_CHOICES, TRANSMISSION_CHOICES


class Car(InstanceStatus):
    """ Characteristics for a car """
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    engine_type = models.CharField(max_length=30, choices=ENGINE_CHOICES, verbose_name='Engine type')
    transmission = models.CharField(max_length=30, choices=TRANSMISSION_CHOICES, verbose_name='Transmission type')
    color = models.CharField(max_length=30, choices=COLOR_CHOICES, verbose_name='Color')
    description = models.TextField()

    def __str__(self):
        return f'{self.car_brand} {self.car_model} {self.color}'
