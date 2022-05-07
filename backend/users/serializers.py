from djoser.serializers import UserSerializer, UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password',)


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name',)