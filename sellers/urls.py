from django.urls import path
from .views import SellerProfileView

urlpatterns = [
    path("", SellerProfileView.as_view()),
]