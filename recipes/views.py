from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Category, Ingredient

# Create your views here.
#_______________________________Category___________________________
class CategoryListView(ListView):
    template_name = "recipes/category/list.html"
    model = Category
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    template_name = "recipes/category/detail.html"
    model = Category
    context_object_name = "category"


class CategoryCreateView(CreateView):
    template_name = "recipes/category/form.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(UpdateView):
    template_name = "recipes/category/form.html"
    model = Category
    fields = ["name", "description"]
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(DeleteView):
    template_name = "recipes/category/delete.html"
    model = Category
    success_url = reverse_lazy("category_list")


#_______________________________Ingredient__________________________
class IngredientListView(ListView):
    template_name = "recipes/ingredients/list.html"
    model = Ingredient
    context_object_name = "ingredients"


class IngredientDetailView(DetailView):
    template_name = "recipes/ingredients/detail.html"
    model = Ingredient
    context_object_name = "ingredient"


class IngredientCreateView(CreateView):
    template_name = "recipes/ingredients/form.html"
    model = Ingredient
    fields = ["name", "description"]
    success_url = reverse_lazy("ingredient_list")


class IngredientUpdateView(UpdateView):
    template_name = "recipes/ingredients/form.html"
    model = Ingredient
    fields = ["name", "description"]
    success_url = reverse_lazy("ingredient_list")


class IngredientDeleteView(DeleteView):
    template_name = "recipes/ingredients/delete.html"
    model = Ingredient
    success_url = reverse_lazy("ingredient_list")
