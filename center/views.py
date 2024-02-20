from .serializers import CenterSerializer
from .models import Center
from rest_framework import generics


# by id - get, update, delete
class CenterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer


class CenterList(generics.ListCreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

