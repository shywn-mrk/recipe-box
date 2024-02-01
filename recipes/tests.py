from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Recipe


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="password"
        )
        self.category = Category.objects.create(name="Test Category")
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="Test ingredients",
            country="US",
            method="Test method",
            cook_duration_minutes=30,
            user=self.user,
            servings=4,
        )
        self.recipe.categories.add(self.category)

    def test_recipe_list_view(self):
        response = self.client.get(reverse("recipes:discover"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_list.html")

    def test_user_recipe_list_view_unauthenticated(self):
        response = self.client.get(reverse("recipes:list"))
        self.assertEqual(response.status_code, 302)

    def test_user_recipe_list_view_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("recipes:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_list.html")

    def test_recipe_detail_view(self):
        response = self.client.get(
            reverse("recipes:detail", kwargs={"pk": self.recipe.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["recipe"], self.recipe)
        self.assertTemplateUsed(response, "recipes/recipe_detail.html")

    def test_recipe_create_view_unauthenticated(self):
        response = self.client.get(reverse("recipes:add"))
        self.assertEqual(response.status_code, 302)

    def test_recipe_create_view_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("recipes:add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_form.html")

    def test_recipe_update_view_unauthenticated(self):
        response = self.client.get(
            reverse("recipes:update", kwargs={"pk": self.recipe.pk})
        )
        self.assertEqual(response.status_code, 302)

    def test_recipe_update_view_authenticated(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(
            reverse("recipes:update", kwargs={"pk": self.recipe.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_update.html")

    def test_recipe_delete_view_unauthenticated(self):
        response = self.client.get(
            reverse("recipes:delete", kwargs={"pk": self.recipe.pk})
        )
        self.assertEqual(response.status_code, 302)

    def test_recipe_search(self):
        response = self.client.get(
            reverse("recipes:discover")
            + "?name=test&country=US&ingredients=flour"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/recipe_list.html")
