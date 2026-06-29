from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User
from .models import SellerProfile


@receiver(post_save, sender=User)
def create_seller_profile(sender, instance, created, **kwargs):

    if created and instance.role == User.SELLER:
        SellerProfile.objects.create(
            user=instance,
            shop_name=f"{instance.username}'s Shop"
        )