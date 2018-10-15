from rest_framework import viewsets, generics, status
from .serializers import *
from monitoring.app_common.components import Pager
from .search_filter import *
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

# Create your views here.

class DeviceViewSet(viewsets.ModelViewSet, generics.ListAPIView, UpdateModelMixin):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    pagination_class = Pager
    filter_backends = (DeviceFilter, OrderingFilter)
    ordering_fields = ('id', 'name')
    filter_fields = ordering_fields
    search_fields = ordering_fields
    ordering = 'name'

class VendorViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    pagination_class = Pager
    filter_backends = (VendorFilter, OrderingFilter)
    ordering_fields = ('id', 'name')
    filter_fields = ordering_fields
    search_fields = ordering_fields
    ordering = 'name'