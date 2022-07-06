from rest_framework import routers
from buyers.urls import buyers_router
from dealers.urls import dealers_router
from suppliers.urls import suppliers_router


router = routers.DefaultRouter()
router.registry.extend(buyers_router.registry)
router.registry.extend(dealers_router.registry)
router.registry.extend(suppliers_router.registry)
