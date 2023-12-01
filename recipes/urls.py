from django.urls import path

from .views import recipe_add, recipe_detail, recipe_list, recipe_list_discover

app_name = "recipes"
urlpatterns = [
    path("", recipe_list, name="list"),
    path("discover/", recipe_list_discover, name="discover"),
    path("add/", recipe_add, name="add"),
    path("<int:pk>/", recipe_detail, name="detail"),
]
