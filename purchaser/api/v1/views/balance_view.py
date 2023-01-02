from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from purchaser.api.v1.serializers.balance_serializer import BalanceSerializer
from purchaser.models import Balance


class APIListPaginationPurchaser(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 15


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    pagination_class = APIListPaginationPurchaser
