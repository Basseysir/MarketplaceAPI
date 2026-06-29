from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.models import SellerOrder

# Create your views here.

class SellerDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role != "seller":
            return Response(
                {"error": "Only sellers can access dashboard"},
                status=403
            )

        seller = request.user.seller_profile

        orders = SellerOrder.objects.filter(
            seller=seller
        )

        revenue = orders.aggregate(
            total=Sum("subtotal")
        )["total"] or 0

        return Response({
            "shop_name": seller.shop_name,
            "total_products": seller.products.count(),
            "total_orders": orders.count(),
            "total_revenue": revenue,
            "pending_orders": orders.filter(
                status="pending"
            ).count(),
            "shipped_orders": orders.filter(
                status="shipped"
            ).count(),
            "delivered_orders": orders.filter(
                status="delivered"
            ).count(),
        })