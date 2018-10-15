from django.conf.urls import url, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from .views import *

router = routers.DefaultRouter()
router.register(r'device', DeviceViewSet)
router.register(r'vendor', VendorViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]