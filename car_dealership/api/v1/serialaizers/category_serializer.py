from rest_framework import serializers

from car_dealership.models import Category

class CategorySerializers(serializers.ModelSerializers):
    class Meta:
        model = Category
        fields = ['name']