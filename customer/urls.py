from django.urls import path
from .views import CustomerDetail, CustomerList


urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customers'),
    path('customer/<int:pk>', CustomerDetail.as_view(), name='customer'),
]
