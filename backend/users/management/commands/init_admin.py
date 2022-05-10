import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SU_ADMIN", "test_admin")
        email = os.environ.get("DJANGO_SU_EMAIL", "test_admin@mail.com")
        password = os.environ.get("DJANGO_SU_PASSWORD", "qwerty1234")
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role="admin",
            )
