from django.urls import include, path
import buyers.views as views
from rest_framework import routers


buyers_router = routers.DefaultRouter()
buyers_router.register(r'buyers', views.BuyersViewSet, basename='buyers')
buyers_router.register(r'buyers_history', views.BuyerHistoryViewSet, basename='buyers_history')
buyers_router.register(r'buyers_offer', views.BuyerOfferViewSet, basename='buyers_offer')

urlpatterns = [
    path('buyer/', include(buyers_router.urls))
]
