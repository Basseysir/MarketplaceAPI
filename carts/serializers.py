from rest_framework import serializers
from .models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    subtotal = serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ["id", "product", "product_name", "quantity", "subtotal"]
    def get_subtotal(self, obj):
        return obj.subtotal

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = ["id", "user", "total", "items"]
    def get_total(self, obj):
        return sum(item.subtotal for item in obj.items.all())