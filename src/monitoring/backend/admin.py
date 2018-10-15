from django.contrib import admin
from django.forms import ModelForm, PasswordInput
from .models import *


# Register your models here.
class DeviceAdminForm(ModelForm):
    class Meta:
        widgets = {
            'password': PasswordInput(),
        }

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm
    @staticmethod
    def vendor_name(model):
        return model.vendor.name
    list_display = ('name', 'vendor_name', 'location')


@admin.register(DeviceReport)
class DeviceReportAdmin(admin.ModelAdmin):
    @staticmethod
    def location(model):
        return model.device.location
    list_display = ('device','location','status','temperature','flag')
