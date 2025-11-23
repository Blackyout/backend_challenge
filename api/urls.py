from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]