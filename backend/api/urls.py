from django.urls import include, path
from rest_framework import routers

from api.views import IngredientsViewSet, RecipeViewSet, TagViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"ingredients", IngredientsViewSet, basename="ingredients")

urlpatterns = [
    path("", include(router.urls)),
]
