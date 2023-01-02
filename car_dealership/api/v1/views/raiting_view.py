from rest_framework import viewsets

from car_dealership.api.v1.serializers.raiting_serializer import RaitingSerializer
from car_dealership.api.v1.views.car_dealership_view import APIListPagination
from car_dealership.models import Raiting


class RaitingViewSet(viewsets.ModelViewSet):
    queryset = Raiting.objects.all().order_by('value')
    serializer_class = RaitingSerializer
    pagination_class = APIListPagination