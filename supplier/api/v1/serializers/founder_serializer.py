from rest_framework import serializers

from supplier.models import Founder

class FounderSerializers(serializers.ModelSerializers):
    class Meta:
        model = Founder
        fields = ['first_name', 'second_name', 'age', 'company']