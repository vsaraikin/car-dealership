from django.contrib import admin
from .models import Buyers, BuyerHistory, BuyerOffer


class BuyersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'balance')


class BuyerHistoryAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'car', 'price', 'date_bought')


admin.site.register(Buyers, BuyersAdmin)
admin.site.register(BuyerHistory, BuyerHistoryAdmin)
admin.site.register(BuyerOffer)
