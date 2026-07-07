from django.conf import settings
from django.db import models
from products.models import Product

class Order(models.Model):
    """Represents a buyer's full checkout order."""
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order #{self.id}"

class SellerOrder(models.Model):
    """Represents the portion of an Order that belongs to one seller."""
    PENDING, PROCESSING, SHIPPED, DELIVERED = "pending", "processing", "shipped", "delivered"
    STATUS_CHOICES = ((PENDING, "Pending"), 
                    (PROCESSING, "Processing"), 
                    (SHIPPED, "Shipped"), 
                    (DELIVERED, "Delivered"))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="seller_orders")
    seller = models.ForeignKey("sellers.SellerProfile", on_delete=models.CASCADE, related_name="orders")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Seller Order #{self.id}"

class OrderItem(models.Model):
    """A line item linking a single product to a SellerOrder."""
    seller_order = models.ForeignKey(SellerOrder, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product.name
