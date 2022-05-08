from djoser.views import UserViewSet
from django.contrib.auth import get_user_model

from users.serializers import CustomUserSerializer

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()
