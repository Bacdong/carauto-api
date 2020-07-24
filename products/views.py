from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import GetAllProductInfo, ProductSerializer

# Create your views here.
class GetAllProductInfoAPIView(APIView):

    def get(self, request):
    
        list_product = Products.objects.all()
        my_data = GetAllProductInfo(list_product, many = True)

        return Response(data = my_data.data, status = status.HTTP_200_OK)

    def post(self, request):
        my_data = ProductSerializer(data = request.data)

        if not my_data.is_valid():
            return Response(
                'Error: Product info is valid! Try again!', 
                status = status.HTTP_400_BAD_REQUEST
            )

        name = my_data.data['name']
        description = my_data.data['description']
        price = my_data.data['price']
        category = my_data['category']
        # status = my_data.data['status']

        new_product = Products.objects.create(
            name = name, 
            description = description,
            price = price,
            category = category,
            # status = status,
        )

        return Response(
            'Add product successfully!',
            data = new_product.id, 
            status = status.HTTP_200_OK
        )