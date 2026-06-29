from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSeller, IsOwnerSeller
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    parser_classes = [JSONParser, MultiPartParser, FormParser,]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsSeller(), IsOwnerSeller()]
        return super().get_permissions()
    
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_class = ProductFilter

    search_fields = [
        'name',
        'description'
    ]

    ordering_fields = [
        'price',
        'created_at',
        'stock'
    ]

    def perform_create(self, serializer):
        serializer.save(
            seller=self.request.user.seller_profile
        )