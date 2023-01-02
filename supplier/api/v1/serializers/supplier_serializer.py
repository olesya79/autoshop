from rest_framework import serializers

from supplier.models import Supplier

class SupplierSerializers(serializers.ModelSerializers):
    class Meta:
        model = Supplier
        fields = ['name', 'location', 'contact', 'auto']