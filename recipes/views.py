from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import RecipeForm, RecipeSearchForm
from .models import Recipe


class UserRecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    paginate_by = 15

    def get_queryset(self):
        form = RecipeSearchForm(self.request.GET)
        queryset = Recipe.objects.filter(user=self.request.user).order_by(
            "-created_at"
        )

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes_count"] = self.get_queryset().count()
        context["form"] = RecipeSearchForm(initial=self.request.GET)
        return context


class RecipeListView(ListView):
    model = Recipe
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes_count"] = self.get_queryset().count()
        context["form"] = RecipeSearchForm(initial=self.request.GET)
        return context

    def get_queryset(self):
        form = RecipeSearchForm(self.request.GET)
        queryset = Recipe.objects.order_by("-created_at")

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


class RecipeDetailView(DetailView):
    model = Recipe


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # type: ignore
    model = Recipe
    success_url = reverse_lazy("recipes:list")

    def test_func(self):
        return self.get_object().user == self.request.user

    def post(self, request, *args, **kwargs):
        messages.success(
            self.request,
            f"Recipe with the name of {self.get_object().name} successfully deleted.",
        )
        return super().delete(request, *args, **kwargs)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:list")
    template_name = "recipes/recipe_update.html"

    def form_valid(self, form):
        form.instance.updated_at = datetime.now()
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().user == self.request.user


class IndexView(TemplateView):
    template_name = "index.html"
