from django.contrib import admin
from .models import Author, Recipe

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Recipe, RecipeAdmin)
