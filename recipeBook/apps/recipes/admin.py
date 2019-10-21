from django.contrib import admin
from .models import RecipeType, Recipe, Comment


admin.site.register(RecipeType)

admin.site.register(Recipe)

admin.site.register(Comment)