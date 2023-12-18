from django import forms
from django_countries.data import COUNTRIES

from recipes.models import Recipe


class RecipeSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="Recipe Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter recipe name"}
        ),
    )
    country = forms.ChoiceField(
        choices=COUNTRIES.items(),
        required=False,
        label="Country",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    ingredients = forms.CharField(
        required=False,
        label="Ingredients",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter ingredients"}
        ),
    )


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ["user", "updated_at"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter recipe name",
                }
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter ingredients",
                }
            ),
            "country": forms.Select(attrs={"class": "form-select"}),
            "categories": forms.CheckboxSelectMultiple(
                attrs={"class": "form-check-input"}
            ),
            "method": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter cooking method",
                }
            ),
            "cook_duration_minutes": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter cooking duration in minutes",
                }
            ),
            "servings": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter servings"}
            ),
        }
