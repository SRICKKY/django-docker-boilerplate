# models.py
from django.contrib.auth.models import User
from django.db import models

from shopnest.models import (
    Category,
    Order,
    PaymentMethod,
    Product,
    ReviewAndRating,
    ShippingAddress,
    Wishlist,
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlists = models.ManyToManyField(Wishlist, blank=True)
    payment_methods = models.ManyToManyField(PaymentMethod, blank=True)
    shipping_addresses = models.ManyToManyField(ShippingAddress, blank=True)
    order_history = models.ManyToManyField(Order, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    reviews_and_ratings = models.ManyToManyField(Product, through=ReviewAndRating)
    recommended_categories = models.ManyToManyField(Category, blank=True)
    communication_preferences = models.TextField(blank=True)
    shopping_lists = models.ManyToManyField(Wishlist, related_name='shoppers', blank=True)
    prime_member = models.BooleanField(default=False)
    notifications = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username