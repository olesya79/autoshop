from rest_framework import viewsets

from supplier.api.v1.serializers.founder_serializer import FounderSerializer
from supplier.api.v1.views.supplier_view import APIListPaginationPurchaser
from supplier.models import Founder


class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    pagination_class = APIListPaginationPurchaser