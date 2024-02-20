from .serializers import InvoiceSerializer
from .models import Invoice
from rest_framework import generics


# by id - get, update, delete
class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceList(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
