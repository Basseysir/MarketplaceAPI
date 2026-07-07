from django.urls import path
from .views import CartView, AddToCartView, CartItemDetailView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add/", AddToCartView.as_view(), name="add-to-cart"),
    path("item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item"),
]


# path("item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item") 
# creates a dynamic URL for a specific cart item. The <int:pk> 
# captures the item's ID from the URL, CartItemDetailView.as_view() 
# tells Django which class should process the request, and 
# name="cart-item" gives the URL a reusable name inside the project.