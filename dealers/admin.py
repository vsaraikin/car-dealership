from django.contrib import admin
from .models import Dealers, Dealer, DealerToBuyer, SupplierToDealer, DealerPromotion


class DealersAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'balance', 'characteristics_of_car')


class DealerAdmin(admin.ModelAdmin):
    list_display = ('dealer', 'car', 'car_count', 'price')


admin.site.register(Dealers)
admin.site.register(Dealer)
admin.site.register(DealerToBuyer)
admin.site.register(SupplierToDealer)
admin.site.register(DealerPromotion)
