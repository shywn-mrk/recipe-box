from django.shortcuts import render

from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()

    context = {"recipes": recipes, "recipes_count": recipes.count()}

    return render(request, "recipes/recipe_list.html", context=context)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    context = {"recipe": recipe}

    return render(request, "recipes/recipe_detail.html", context=context)
