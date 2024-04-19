from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

# by id - get, update, delete
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# @extend_schema(responses=ProductSerializer)
@api_view(['GET'])
def getProduct(request):
    # person = {'name': 'elivia kabigumila', 'age': 27}
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
#
#
#
# @api_view(['POST'])
# def addProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
