from django.urls import path

from .views import recipe_detail, recipe_list

urlpatterns = [
    path("", recipe_list, name="recipe-list"),
    path("<int:pk>/", recipe_detail, name="recipe-detail"),
]
