from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect

from .models import Recipe, Author
from .forms import RecipeAddForm, AuthorAddForm


def index(request):
    imageSrc = "https://images.unsplash.com/photo-1496262967815-132206202600?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2295&q=80"
    recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html', {'recipes': recipes, 'imageSrc': imageSrc})


def recipe_detail(request, recipe_id):
    imageSrc = "https://images.unsplash.com/photo-1496262967815-132206202600?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2295&q=80"
    html = 'recipe/recipeDetail.html'
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, html, {'recipe': recipe, 'imageSrc': imageSrc})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    recipes = Recipe.objects.all()
    return render(request, 'recipe/authorDetail.html', {
        'author': author,
        'recipes': recipes,
    })


def add_author_view(request):
    html = "generic_form.html"
    form = AuthorAddForm()
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("recipes:index"))

    return render(request, html, {'form': form})


def add_recipe_view(request):
    html = "generic_form.html"
    form = RecipeAddForm()
    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("recipes:index"))

    return render(request, html, {'form': form})


def delete_recipe(request, recipe_id):
    html = "recipe/recipeDelete.html"
    recipe_to_delete = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        recipe_to_delete.delete()
        return HttpResponseRedirect(reverse("recipes:index"))

    return render(request, html)


def update_recipe(request, recipe_id):
    html = "generic_form.html"
    recipe = Recipe.objects.get(id=recipe_id)

    form = RecipeAddForm(instance=recipe)
    if request.method == "POST":
        form = RecipeAddForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("recipes:index"))
    return render(request, html, {'form': form})
