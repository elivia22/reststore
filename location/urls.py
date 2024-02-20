from django.urls import path
from .views import LocationDetail, LocationList


urlpatterns = [
    path('locations/', LocationList.as_view(), name='locations'),
    path('location/<int:pk>', LocationDetail.as_view(), name='location'),
]
