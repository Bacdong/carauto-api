from django.db import models
from rest_framework import serializers

# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    status = models.BooleanField(default = True)


class Products(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    price = models.IntegerField(default = 0)
    status = models.BooleanField(default = True)


class Variation(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    sale_price = models.IntegerField(default = 0)
    inventory = models.IntegerField(default = 0)
    status = models.BooleanField(default = True)