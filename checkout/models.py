from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from products.models import Product
from cart.models import OrderLineItem


# Save Users address to the database
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=30)
    postcode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name},{self.address_line_1},{self.address_line_2},{self.town},{self.county},{self.postcode}"


# Save users order details to the database
class Order(models.Model):
    orderitems = models.ManyToManyField(OrderLineItem)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=200, blank=True, null=True)
    orderId = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,
                                blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()

        return total
