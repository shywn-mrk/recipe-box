from django.urls import path

from .views import recipe_detail, recipe_list

app_name = "recipes"
urlpatterns = [
    path("", recipe_list, name="list"),
    path("<int:pk>/", recipe_detail, name="detail"),
]
