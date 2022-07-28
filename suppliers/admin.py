from django.contrib import admin
from .models import Suppliers, Supplier, SupplierPromotion, SupplierStatistic

admin.site.register(Suppliers)
admin.site.register(Supplier)
admin.site.register(SupplierPromotion)
admin.site.register(SupplierStatistic)
