# Generated by Django 4.2.7 on 2023-12-29 07:33

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_category_remove_recipe_category_recipe_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/images'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
