from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import SellerProfile
from .serializers import SellerProfileSerializer


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