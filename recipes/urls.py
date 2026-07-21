from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    IngredientListView,
    IngredientDetailView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
)

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/new/", CategoryCreateView.as_view(), name="category_new"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category_edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),

    path("ingredients/", IngredientListView.as_view(), name="ingredient_list"),
    path("ingredients/new/", IngredientCreateView.as_view(), name="ingredient_new"),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name="ingredient_detail"),
    path("ingredients/<int:pk>/edit/", IngredientUpdateView.as_view(), name="ingredient_edit"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient_delete"),
]
