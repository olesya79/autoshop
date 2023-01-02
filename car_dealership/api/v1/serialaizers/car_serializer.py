from rest_framework import serializers

from car_dealership.models import Car

class CarSerializers(serializers.ModelSerializers):
    class Meta:
        model = Car
        fields = ['title', 'price', 'currency', 'cat']