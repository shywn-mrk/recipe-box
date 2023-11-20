from django.db import models


class IranianFoodManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(country="Iran")
