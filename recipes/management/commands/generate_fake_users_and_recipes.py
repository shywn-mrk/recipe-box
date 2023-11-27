from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django_countries import countries
from faker import Faker

from recipes.models import Category, Recipe

User = get_user_model()


class Command(BaseCommand):
    help = "Generate fake users and recipes"

    def add_arguments(self, parser):
        parser.add_argument(
            "total_users",
            type=int,
            help="Indicates the number of fake users to be created",
        )
        parser.add_argument(
            "total_recipes",
            type=int,
            help="Indicates the number of fake recipes to be created",
        )

    def handle(self, *args, **kwargs):
        total_users = kwargs["total_users"]
        total_recipes = kwargs["total_recipes"]

        self.stdout.write(
            self.style.SUCCESS(f"Generating {total_users} fake users...")
        )
        self.generate_fake_users(total_users)

        self.stdout.write(
            self.style.SUCCESS(f"Generating {total_recipes} fake recipes...")
        )
        self.generate_fake_recipes(total_recipes)

        self.stdout.write(self.style.SUCCESS("Fake data generation complete."))

    def generate_fake_users(self, total_users):
        for i in range(total_users):
            fake = Faker()
            username = fake.user_name() + str(i)
            email = fake.email()
            password = get_random_string(length=12)
            User.objects.create_user(username=username, email=email, password=password)  # type: ignore

    def generate_fake_recipes(self, total_recipes):
        country_codes = [country[0] for country in countries]

        categories = Category.objects.all()

        for _ in range(total_recipes):
            fake = Faker()
            name = fake.word()
            ingredients = fake.text()
            country = fake.random_element(country_codes)
            method = fake.text()
            cook_duration_minutes = fake.random_int(min=5, max=120)
            servings = fake.random_int(min=1, max=10)

            user = User.objects.order_by("?").first()

            recipe = Recipe.objects.create(
                name=name,
                ingredients=ingredients,
                country=country,
                method=method,
                cook_duration_minutes=cook_duration_minutes,
                user=user,
                servings=servings,
            )

            recipe.categories.set(
                categories.order_by("?")[: fake.random_int(min=1, max=3)]
            )
