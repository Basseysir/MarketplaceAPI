from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    seller = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"