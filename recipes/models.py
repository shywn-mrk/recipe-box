from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField

from .managers import IranianFoodManager

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    ingredients = models.TextField()
    country = CountryField()
    categories = models.ManyToManyField(Category)
    method = models.TextField()
    cook_duration_minutes = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    user_recipes: models.Manager = IranianFoodManager()

    def __str__(self) -> str:
        return self.name
