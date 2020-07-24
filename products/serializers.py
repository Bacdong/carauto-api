from rest_framework import serializers
from .models import Products

class GetAllProductInfo(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    description = serializers.CharField(max_length = 200)
    category = serializers.IntegerField()
    price = serializers.IntegerField(default = 0)
    # status = serializers.BooleanField(default = True)