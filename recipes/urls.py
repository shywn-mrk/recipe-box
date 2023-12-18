from django.urls import path

from .views import (
    RecipeAddView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    UserRecipeListView,
)

app_name = "recipes"
urlpatterns = [
    # path("", recipe_list, name="list"),
    path("", UserRecipeListView.as_view(), name="list"),
    # path("discover/", recipe_list_discover, name="discover"),
    path("discover/", RecipeListView.as_view(), name="discover"),
    path("add/", RecipeAddView.as_view(), name="add"),
    # path("<int:pk>/", recipe_detail, name="detail"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", RecipeDeleteView.as_view(), name="delete"),
]
