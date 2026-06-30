from rest_framework import serializers
from .models import SellerProfile


class SellerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellerProfile
        fields = [
            "id",
            "shop_name",
            "bio",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]