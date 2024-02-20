from django.urls import path
from django import urls
from . import views
from .views import UserCreate
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # path('', CurrentUserView.as_view(), name='user'),
    path('registration', UserCreate.as_view(), name='registration'),

    # path('login/', name='login'),
    # path('logout/', name='logout'),
    # path('password_change/', name='password_change'),
    # path('password_change/done/', name='password_change_done'),
    # path('password_reset/', name='password_reset'),
    # path('password_reset/done/', name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # path('reset/done/', name='password_reset_complete'),
]
