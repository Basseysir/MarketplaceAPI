from django.shortcuts import render
from orders.models import SellerOrder
from products.models import Product
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import SellerProfile
from .serializers import SellerProfileSerializer



# Create your views here.

class SellerProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        seller = request.user.seller_profile

        serializer = SellerProfileSerializer(seller)

        return Response(serializer.data)


    def post(self, request):

        if hasattr(request.user, "seller_profile"):
            return Response(
                {"error": "Seller profile already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SellerProfileSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


    def patch(self, request):

        seller = request.user.seller_profile

        serializer = SellerProfileSerializer(
            seller,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)


class SellerDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        seller = request.user.seller_profile

        total_products = Product.objects.filter(
            seller=seller
        ).count()

        total_orders = SellerOrder.objects.filter(
            seller=seller
        ).count()

        pending_orders = SellerOrder.objects.filter(
            seller=seller,
            status="pending"
        ).count()

        processing_orders = SellerOrder.objects.filter(
            seller=seller,
            status="processing"
        ).count()

        delivered_orders = SellerOrder.objects.filter(
            seller=seller,
            status="delivered"
        ).count()

        revenue = sum(
            order.subtotal
            for order in SellerOrder.objects.filter(
                seller=seller,
                status="delivered"
            )
        )

        return Response({
            "total_products": total_products,
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "processing_orders": processing_orders,
            "delivered_orders": delivered_orders,
            "revenue": revenue
        })