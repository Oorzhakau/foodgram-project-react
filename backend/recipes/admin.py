from django.contrib import admin

from .models import Recipe, Ingredient, Tag, FavoriteRecipe


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "slug", "name", "color",)
    list_display_links = ("pk", "slug",)
    list_editable = ("name",)
    search_fields = ("slug", "name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "measurement_unit")
    list_display_links = ("pk", "name",)
    list_editable = ("measurement_unit",)
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "author", "cooking_time", "favorites",)
    list_display_links = ("pk", "name",)
    list_filter = ("author", "name", "tags",)
    search_fields = ("author", "name",)
    empty_value_display = "-пусто-"

    @staticmethod
    def favorites(obj):
        return obj.favorite.filter(favorite=True).count()


@admin.register(FavoriteRecipe)
class FavoriteAdmin(admin.ModelAdmin):
    autocomplete_fields = ('recipe', )
    list_display = ('pk', 'user', 'shopping_cart', 'favorite')