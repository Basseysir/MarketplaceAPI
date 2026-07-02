from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CartItem
from .serializers import CartSerializer
from products.models import Product

# Create your views here.

class CartView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = CartSerializer(request.user.cart)

        return Response(serializer.data)


class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        product = get_object_or_404(Product, id=product_id)

        item, created = CartItem.objects.get_or_create(
            cart=request.user.cart,
            product=product
        )

        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity

        item.save()

        return Response(
            {"message": "Added to cart"},
            status=status.HTTP_201_CREATED
        )

class CartItemDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        item = get_object_or_404(
            CartItem,
            id=pk,
            cart=request.user.cart
        )

        quantity = request.data.get("quantity")

        if quantity:
            item.quantity = quantity
            item.save()

        return Response(
            {"message": "Cart updated"}
        )

    def delete(self, request, pk):

        item = get_object_or_404(
            CartItem,
            id=pk,
            cart=request.user.cart
        )

        item.delete()

        return Response(
            {"message": "Item removed"}
        )