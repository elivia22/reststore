from django.urls import path
from .views import OrderDetail, OrderList

urlpatterns = [
    path('', OrderList.as_view(), name='orders'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order'),
]



