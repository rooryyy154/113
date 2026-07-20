from django.contrib import admin
from .models import Category, Ingredient, RecipeIngredient, Recipe

admin.site.register([Category, Ingredient, RecipeIngredient, Recipe])

# Register your models here.
