from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    CATEGORIES_CHOICES = [
        ("Breakfast", "Breakfast"),
        ("Lunch", "Lunch"),
        ("Dinner", "Dinner"),
        ("Dessert", "Dessert"),
    ]

    name = models.CharField(max_length=150)
    ingredients = models.TextField()
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
    method = models.TextField()
    cook_duration_minutes = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(blank=True, null=True)
