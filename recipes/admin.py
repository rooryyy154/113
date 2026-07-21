from django.contrib import admin
from .models import Category, Ingredient, RecipeIngredient, Recipe

# admin.site.register([Category, Ingredient, RecipeIngredient, Recipe])

# Register your models here.
#_______________________________Category_________________________
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('name', 'slug','recipe_count')

    search_fields = ('name',)

    prepopulated_fields = {'slug':('name',)}

    @admin.display(description="# Recipes")
    def recipe_count(self, obj):
        return obj.recipes.count()
    
#_______________________________Ingredient________________________
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

#________________________RecipeIngredient__________________________
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 3 # how many empty rows to show by default
    fields = ('ingredients', 'quantity','unit','notes')


#________________________Recipe____________________________________
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','category','status','prep_time','created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('title', 'description', 'author_username')
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RecipeIngredientInline]

    fieldsets = (
        ('Main Information', {
            'fields': ("title", 'slug', 'author', 'category', 'status')
        }),
        ('Content', {
            'fields': ('description', 'instructions', 'image')
        }),
        ('Time & Servings', {
            'fields': ('prep_time', 'cook_time', 'servings')
        }),
        ('Timestamps', {
            'fields':('created_at', 'updated_at'),
            'classes':('collapse',)
        }),
    )



