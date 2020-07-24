from django.db import models
from users.models import CustomerUser
from carts.models import Carts

# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete = models.CASCADE)
    cart = models.ForeignKey(Carts, on_delete = models.CASCADE)
    shipping_address = models.CharField(max_length = 255)
    order_description = models.TextField(default = '')
    is_completed = models.BooleanField(default = False)
