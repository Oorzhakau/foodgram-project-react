from django_filters import rest_framework as filters

from django.db.models import Sum, Count
from recipes.models import Recipe, Tag, IngredientsInRecipes
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
import datetime as dt

from api.filters import RecipeFilter
from api.paginations import CustomPageSizePagination
from api.permissions import AdminOrAuthorOrReadOnly
from api.serializers import RecipeSerializer, TagSerializer
from utils.create_pdf_file import create_pdf
from collections import defaultdict


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

    @action(
        detail=False,
        permission_classes=[IsAuthenticated],
        url_path='download_shopping_cart',
    )
    def get_shopping_cart(self, request):
        shopping_cart_to_download = IngredientsInRecipes.objects.filter(
            recipe__favorite__user=self.request.user,
            recipe__favorite__shopping_cart=True,
        ).values(
            'ingredient__name',
            'ingredient__measurement_unit',
            'amount',
        )

        obj_dic = {
            'file_name': '%s_%s.pdf' % (
                dt.datetime.utcnow().strftime('%Y-%m-%d'),
                self.request.user.username,
            ),
            'doc_title': 'FOODGRAM',
            'title': 'Список покупок',
            'user': 'Пользователь: %s %s' % (
                self.request.user.last_name,
                self.request.user.first_name,
            ),
            'text': [],
        }
        data = {}
        for idx, item in enumerate(shopping_cart_to_download):
            name = item["ingredient__name"].capitalize()
            unit = item["ingredient__measurement_unit"]
            amount = item["amount"]
            if name not in data:
                data[name] = [amount, unit]
                continue
            data[name][0] += amount

        for idx, (key, value) in enumerate(data.items()):
            obj_dic['text'].append(
                f'{idx + 1}. {key} - 'f'{value[0]} 'f'{value[1]}'
            )
        return create_pdf(obj_dic)
