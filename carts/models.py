from django.db import models
from products.models import Variation
from users.models import CustomerUser

# Create your models here.
class Carts(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    update_add = models.DateTimeField(auto_now = True)

class CartItems(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete = models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete = models.CASCADE)
    item = models.ForeignKey(Variation, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)