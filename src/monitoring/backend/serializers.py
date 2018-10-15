from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'name', 'address')

class DeviceSerializer(serializers.ModelSerializer):
    vendor = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        vendor_id = serializers.SlugRelatedField(read_only=True, slug_field='id')
        model = Device
        fields = ('id','name', 'vendor', 'vendor_id', 'location', 'lat', 'long', 'status')

class DeviceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceReport
        device = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        fields = (device, 'status', 'power', 'flag', 'temperature', 'last_update')