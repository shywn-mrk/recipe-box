from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView

from .models import Recipe


@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)

    context = {"recipes": recipes, "recipes_count": recipes.count()}

    return render(request, "recipes/recipe-list.html", context=context)


def recipe_list_discover(request):
    recipes = Recipe.objects.all()

    context = {"recipes": recipes, "recipes_count": recipes.count()}

    return render(request, "recipes/recipe-list.html", context=context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    context = {"recipe": recipe}

    return render(request, "recipes/recipe-detail.html", context=context)


class IndexView(TemplateView):
    template_name = "index.html"
