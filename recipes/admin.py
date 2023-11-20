from django.contrib import admin

from .models import Category, Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "country",
        "cook_duration_minutes",
        "user",
        "servings",
        "created_at",
    )
    list_display_links = ("id", "name")
    list_filter = ("country",)
    search_fields = ("country", "name", "user")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
