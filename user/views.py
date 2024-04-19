from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

@api_view(('POST',))
# def signIn(request):
def signIn(request, username, password):
    # login(request)
    # user = authenticate(request,username=username,password=password)
    # user =  authenticate(username="test", password="secret")
    user = authenticate(username==username, password==password)
    if user is not None:
        login(request, user)

    # if user:
        return Response (
            {
            'msg': 'trueee',
        })
    #     # return messages.success(request,f'You have been logged in.')
    else :
        return Response (
            {
            'msg': 'falseseee',
        })
        # return messages.error(request,f'Invalid username or password')
        

def signOut(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return ('login') 


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args):
    # def post(self, request, *args **kwargs):
        serializer = self.serializer_class(data=request.data, context = {'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response (
            {
            'token': token.key,
            'username': user.username,
            'user_id': user.id,
            'user_email': user.email,
        })
    


class UserCreate(generics.CreateAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = (AllowAny,)
    

# class ProfileView(APIView):
#       permission_classes = [IsAuthenticated]
@api_view(['GET'])
def currentUser(request, format=None):
    content = {
        'username': str(request.user.username),
        'user_id': str(request.user.id),
        'user_email': str(request.user.email),
        'auth': str(request.auth),
    }
    return Response(content)


class IndexView(APIView):
    permission_classes = [IsAuthenticated]
    def get(request, format=None):
        content = {
            'wmsg': 'welcomeeeeeeeeeee',
        }
        return Response(content)
    