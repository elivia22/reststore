from django.urls import path
from django import urls
from . import views
from .views import ProductDetail, ProductList, ProductCreate
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    # path('view/', views.getProduct),
    # path('add/', views.addProduct),
    path('all/', ProductList.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('id/<int:pk>', ProductDetail.as_view(), name='product'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('api/token/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('api/token/', TokenVerifyView.as_view(), name='token_verify_view'),
    # path('login/', obtain_auth_token, name='login'),


    # path('login/', name='login'),
    # path('logout/', name='logout'),
    # path('password_change/', name='password_change'),
    # path('password_change/done/', name='password_change_done'),
    # path('password_reset/', name='password_reset'),
    # path('password_reset/done/', name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # path('reset/done/', name='password_reset_complete'),
]
