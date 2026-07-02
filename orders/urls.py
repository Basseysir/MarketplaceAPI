from django.urls import path
from .views import (
    CheckoutView,
    SellerOrdersView,
    MyOrdersView,
    SellerOrderUpdateView,
)

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("seller-orders/", SellerOrdersView.as_view(), name="seller-orders"),
    path("my-orders/", MyOrdersView.as_view(), name="my-orders"),
    path("seller-orders/<int:pk>/", SellerOrderUpdateView.as_view(), name="seller-order-update"),
]