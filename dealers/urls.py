from django.urls import include, path
import dealers.views as views
from rest_framework import routers


dealers_router = routers.DefaultRouter()
dealers_router.register(r'dealers', views.DealersViewSet, basename='dealers')
dealers_router.register(r'dealer', views.DealerViewSet, basename='dealer')
dealers_router.register(r'supplier_to_dealer', views.SupplierToDealerViewSet, basename='supplier_to_dealer')
dealers_router.register(r'dealer_to_buyer', views.DealerToBuyerViewSet, basename='dealer_to_buyer')
dealers_router.register(r'dealer_promotion', views.DealerPromotionViewSet, basename='dealer_promotion')

urlpatterns = [
    path('dealer/', include(dealers_router.urls))
]
