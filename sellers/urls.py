from django.urls import path
from .views import SellerProfileView, SellerDashboardView

urlpatterns = [
    path("", SellerProfileView.as_view(), name="seller-profile"),
    path("dashboard/", SellerDashboardView.as_view(), name="seller-dashboard"),
]