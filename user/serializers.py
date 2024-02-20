from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)        
        user.set_password(password)
        user.save()
        return {
            "username": user.username,
            "email": user.email
        }

# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     username = serializers.CharField(
#             validators=[UniqueValidator(queryset=User.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)
#     last_name = serializers.CharField(min_length=20)
#     first_name = serializers.CharField(min_length=20)

