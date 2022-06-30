from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'car_model', 'engine_type')


admin.site.register(Car, CarAdmin)
