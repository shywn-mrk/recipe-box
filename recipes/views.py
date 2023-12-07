from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from recipes.forms import RecipeForm, RecipeSearchForm

from .models import Recipe


class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


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


class RecipeListView(ListView):
    model = Recipe
    context_object_name = "recipes"


def recipe_list_discover(request):
    recipes = Recipe.objects.all()
    form = RecipeSearchForm()

    context = {
        "recipes": recipes,
        "recipes_count": recipes.count(),
        "form": form,
    }

    return render(request, "recipes/recipe-list.html", context=context)


class RecipeDetailView(DetailView):
    model = Recipe


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
