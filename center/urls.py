from django.urls import path
from .views import CenterDetail, CenterList


urlpatterns = [
    path('centers/', CenterList.as_view(), name='centers'),
    path('center/<int:pk>', CenterDetail.as_view(), name='center'),
]
