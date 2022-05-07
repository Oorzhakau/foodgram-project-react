from django.contrib import admin

from .models import User, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'username',
        'email',
        'role',
        'first_name',
        'last_name',
    )
    list_display = (
        "pk",
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
    )
    list_display_links = ("pk", "username",)
    list_filter = (
        "username",
        "email",
        ('is_staff', admin.BooleanFieldListFilter),
    )
    search_fields = ("username", "first_name", "last_name",)
    empty_value_display = "-пусто-"
    list_editable = ("role",)
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = (
        "id",
        "username",
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "author",)
    search_fields = ("author",)
