from django.urls import include, path
from rest_framework import routers

from api.views import TagViewSet, RecipeViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"tags", TagViewSet, basename="tags")
router.register(r'recipes', RecipeViewSet, basename="recipes")

urlpatterns = [
    path("", include(router.urls)),
]
