from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
# from .models import user
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny



class UserCreate(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    

# @api_view(['GET'])
# def current_user(request):
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)



# class UserCreate(APIView):
#     def post(self, request, format='json'):
#         return Response('hello')


# @extend_schema(responses=ProductSerializer)
# @api_view(['GET'])
# def getProduct(request):
#     # person = {'name': 'elivia kabigumila', 'age': 27}
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
#
#
# @api_view(['POST'])
# def addProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
