from django.urls import path
from django import urls
from . import views
from .views import UserCreate, IndexView, CustomAuthToken
# from .views import UserCreate, ProfileView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('create/', UserCreate.as_view(), name='create'),
    path('api/auth/', views.CustomAuthToken.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('login/', views.signIn, name='login'),
    path('logout/', views.signOut, name='logout'),
    path('profile/', views.currentUser),

    # path('login/', name='login'),
    # path('logout/', name='logout'),
    # path('password_change/', name='password_change'),
    # path('password_change/done/', name='password_change_done'),
    # path('password_reset/', name='password_reset'),
    # path('password_reset/done/', name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # path('reset/done/', name='password_reset_complete'),
]
