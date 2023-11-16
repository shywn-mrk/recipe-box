# Generated by Django 4.2.7 on 2023-11-16 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ingredients', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Dessert', 'Dessert')], max_length=10)),
                ('method', models.TextField()),
                ('cook_duration_minutes', models.PositiveIntegerField()),
                ('servings', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]