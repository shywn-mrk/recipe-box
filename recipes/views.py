from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import RecipeForm, RecipeSearchForm
from .models import Recipe


class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    paginate_by = 15

    def get_queryset(self):
        form = RecipeSearchForm(self.request.GET)
        queryset = Recipe.objects.filter(user=self.request.user)

        if form.is_valid():
            print("cleaned_data: ", form.cleaned_data)

            if form.cleaned_data["name"]:
                queryset = queryset.filter(
                    name__icontains=form.cleaned_data["name"]
                )

            if form.cleaned_data["country"]:
                queryset = queryset.filter(country=form.cleaned_data["country"])

            if form.cleaned_data["ingredients"]:
                queryset = queryset.filter(
                    ingredients__icontains=form.cleaned_data["ingredients"]
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RecipeSearchForm()
        return context


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
    paginate_by = 15
    ordering = ["created_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RecipeSearchForm()
        return context

    def get_queryset(self):
        form = RecipeSearchForm(self.request.GET)
        queryset = Recipe.objects.all()

        if form.is_valid():
            if form.cleaned_data["name"]:
                queryset = queryset.filter(
                    name__icontains=form.cleaned_data["name"]
                )

            if form.cleaned_data["country"]:
                queryset = queryset.filter(country=form.cleaned_data["country"])

            if form.cleaned_data["ingredients"]:
                queryset = queryset.filter(
                    ingredients__icontains=form.cleaned_data["ingredients"]
                )

        return queryset


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
