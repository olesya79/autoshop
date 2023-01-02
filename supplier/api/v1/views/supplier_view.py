from supplier.api.v1.serializers.supplier_serializer import SupplierSerializer
from supplier.models import Supplier


class APIListPaginationSupplier(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = APIListPaginationPurchaser