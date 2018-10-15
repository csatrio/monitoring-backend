from .models import *
from monitoring.app_common.components import BaseDjangoFilter

class DeviceFilter(BaseDjangoFilter):
    class Meta:
        model = Device
        option = ['exact', 'in', 'startswith']
        fields = {'name': option}

    text_column = ('name', 'location')
    id_column = 'id'

class VendorFilter(BaseDjangoFilter):
    class Meta:
        model = Vendor
        option = ['exact', 'in', 'startswith']
        fields = {'name': option, 'address': option}

    text_column = ('name', 'address')
    id_column = 'id'