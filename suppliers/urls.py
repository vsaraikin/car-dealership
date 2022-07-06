from django.urls import include, path
import suppliers.views as views
from rest_framework import routers


suppliers_router = routers.DefaultRouter()
suppliers_router.register(r'suppliers', views.SuppliersViewSet, basename='suppliers')
suppliers_router.register(r'supplier', views.SupplierViewSet, basename='supplier')
suppliers_router.register(r'supplier_promo', views.SupplierPromotionViewSet, basename='supplier_promo')

urlpatterns = [
    path('supplier/', include(suppliers_router.urls))
]
