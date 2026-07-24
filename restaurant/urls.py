from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking/tables', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
]
