from django.urls import path
from .views import InvoiceDetail, InvoiceList

urlpatterns = [
    path('invoices/', InvoiceList.as_view(), name='invoices'),
    path('invoice/<int:pk>', InvoiceDetail.as_view(), name='invoice'),
]
