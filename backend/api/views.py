from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError
from recipes.models import Tag, Recipe
from api.serializers import TagSerializer, RecipeSerializer
from api.filters import RecipeFilter
from api.permissions import AdminOrAuthorOrReadOnly
from api.paginations import CustomPageSizePagination


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (AdminOrAuthorOrReadOnly,)
    pagination_class = CustomPageSizePagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecipeFilter

    def perform_create(self, serializer):
        if not self.request.data.get('tags'):
            raise ValidationError(
                detail={'tags': ['обязательное поле']}
            )
        serializer.save(
            author=self.request.user,
            tags=self.request.data['tags']
        )

    def perform_update(self, serializer):
        if not self.request.data.get('tags'):
            raise ValidationError(
                detail={'tags': ['обязательное поле']}
            )
        serializer.save(
            author=self.request.user,
            tags=self.request.data['tags']
        )

