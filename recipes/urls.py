from django.urls import path

from .views import (
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    UserRecipeListView,
    recipe_add,
)

app_name = "recipes"
urlpatterns = [
    # path("", recipe_list, name="list"),
    path("", UserRecipeListView.as_view(), name="list"),
    # path("discover/", recipe_list_discover, name="discover"),
    path("discover/", RecipeListView.as_view(), name="discover"),
    path("add/", recipe_add, name="add"),
    # path("<int:pk>/", recipe_detail, name="detail"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="delete"),
]
