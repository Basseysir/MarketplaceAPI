from rest_framework import request
from collections import defaultdict
from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from carts.models import CartItem
from .models import Order, SellerOrder, OrderItem
from .serializers import (
    OrderSerializer,
    SellerOrderSerializer,
    SellerOrderStatusSerializer,
)

# Create your views here.


class CheckoutView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        print(f"\nBuyer: {request.user.email}")

        cart = request.user.cart

        cart_items = (
            cart.items
            .select_related(
                "product",
                "product__seller",
                "product__seller__user",
            )
        )

        if not cart_items.exists():
            return Response(
                {"error": "Cart is empty"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        total = 0

        # Verify stock
        for item in cart_items:

            if item.quantity > item.product.stock:
                return Response(
                    {
                        "error": f"{item.product.name} is out of stock"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            total += item.subtotal

        # Create master order
        order = Order.objects.create(
            buyer=request.user,
            total_amount=total,
            shipping_address=request.data.get(
                "shipping_address",
                "Not Provided",
            ),
        )

        grouped_items = defaultdict(list)

        # Group products by seller
        for item in cart_items:
            grouped_items[item.product.seller].append(item)

        # Create one SellerOrder per seller
        for seller, items in grouped_items.items():

            print(f"\nSeller: {seller.user.email}")

            seller_order = SellerOrder.objects.create(
                order=order,
                seller=seller,
                subtotal=0,
            )

            subtotal = 0

            for item in items:

                OrderItem.objects.create(
                    seller_order=seller_order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )

                item.product.stock -= item.quantity
                item.product.save()

                subtotal += item.subtotal

            seller_order.subtotal = subtotal
            seller_order.save()

            # Seller email
            seller_result = send_mail(
                subject="New Marketplace Order",
                message=f"""
Hello {seller.user.username},

You have received a new order.

Order ID: {order.id}

Subtotal: ${subtotal}

Please log into your dashboard to process this order.
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[seller.user.email],
                fail_silently=False,
            )

            print(f"Seller email sent to {seller.user.email}: {seller_result}")

# Buyer email
            buyer_result = send_mail(
                subject="Order Successful",
                message=f"""
Hello {request.user.username},

Thank you for shopping with us.

Order ID: {order.id}

Total Paid: ${total}

Your order has been received successfully.
""",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[request.user.email],
    fail_silently=False,
)

        print(f"Buyer email sent to {request.user.email}: {buyer_result}")

        cart.items.all().delete()

        return Response(
            {
                "message": "Checkout successful",
                "order_id": order.id,
            },
            status=status.HTTP_201_CREATED,
)
    
class SellerOrdersView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role != "seller":
            return Response(
                {"error": "Only sellers can access"},
                status=403
            )

        orders = SellerOrder.objects.filter(
            seller=request.user.seller_profile
        )

        serializer = SellerOrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)


class MyOrdersView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = Order.objects.filter(
            buyer=request.user
        ).order_by("-created_at")

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)
    
class SellerOrderUpdateView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        seller_order = SellerOrder.objects.get(
            id=pk,
            seller=request.user.seller_profile
        )

        serializer = SellerOrderStatusSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        seller_order.status = serializer.validated_data["status"]
        seller_order.save()

        seller_order.order.status = seller_order.status
        seller_order.order.save()

        return Response({
            "message": "Order updated successfully",
            "status": seller_order.status
        })