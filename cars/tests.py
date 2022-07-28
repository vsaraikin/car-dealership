import pytest
from .models import Car


@pytest.mark.django_db
def test_create_new_car():
    one_car = Car.objects.create(
        car_brand="Lada",
        car_model="Kalina",
        engine_type="Gas",
        transmission="Manual",
        color="Yellow",
        description="Putin's car"
    )
    assert one_car.description == "Putin's car"
