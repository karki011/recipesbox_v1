from django.shortcuts import render, get_object_or_404
from .models import Recipe, Author


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe/recipeDetail.html', {'recipe': recipe})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.all()
    return render(request, 'recipe/authorDetail.html', {
        'author': author,
        'recipes': recipes,
    })
