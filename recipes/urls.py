from django.urls import path

from .views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    RecipeUpdateView,
    UserRecipeListView,
)

app_name = "recipes"
urlpatterns = [
    path("", UserRecipeListView.as_view(), name="list"),
    path("discover/", RecipeListView.as_view(), name="discover"),
    path("add/", RecipeCreateView.as_view(), name="add"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", RecipeDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", RecipeUpdateView.as_view(), name="update"),
]
