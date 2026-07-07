from rest_framework import serializers
from .models import SellerOrder, OrderItem, Order

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    class Meta:
        model = OrderItem
        fields = ["id", "product_name", "quantity", "price"]

class SellerOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = SellerOrder
        fields = ["id", "subtotal", "status", "items"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "total_amount", "status", "created_at"]

class SellerOrderStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=["pending", "processing", "shipped", "delivered"])