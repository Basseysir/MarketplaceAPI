from rest_framework import serializers
from .models import Product
from .models import Category


class ProductSerializer(serializers.ModelSerializer):

    seller = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Category
        fields = "__all__"