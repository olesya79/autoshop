from rest_framework import serializers

from car_dealership.models import Raiting

class RaitingSerializers(serializers.ModelSerializers):
    class Meta:
        model = Raiting
        fields = ['value']