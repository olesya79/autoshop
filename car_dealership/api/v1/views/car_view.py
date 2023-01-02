from rest_framework import viewsets

from car_dealership.api.v1.serializers.car_serializer import CarSerializer
from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from car_dealership.models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('time_create')
    serializer_class = CarSerializer
    pagination_class = APIListPagination