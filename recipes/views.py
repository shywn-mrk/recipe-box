from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from recipes.forms import RecipeForm, RecipeSearchForm

from .models import Recipe


@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)
    form = RecipeSearchForm()

    context = {
        "recipes": recipes,
        "recipes_count": recipes.count(),
        "form": form,
    }

    return render(request, "recipes/recipe-list.html", context=context)


def recipe_list_discover(request):
    recipes = Recipe.objects.all()
    form = RecipeSearchForm()

    context = {
        "recipes": recipes,
        "recipes_count": recipes.count(),
        "form": form,
    }

    return render(request, "recipes/recipe-list.html", context=context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    context = {"recipe": recipe}

    return render(request, "recipes/recipe-detail.html", context=context)


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.user = request.user
            new_recipe.save()
            return redirect("recipes:list")
    else:
        form = RecipeForm()

    return render(request, "recipes/recipe-add.html", {"form": form})


class IndexView(TemplateView):
    template_name = "index.html"
