from django.urls import path
from .views import CartView, AddToCartView, CartItemDetailView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path("item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item"),
]