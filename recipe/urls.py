from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('author/<int:author_id>/', views.author_detail, name="authorDetail"),
    path('recipe/add/', views.add_recipe_view, name="add_recipe"),
    path('author/add/', views.add_author_view, name="add_author"),
    path('recipe/delete/<int:recipe_id>/',
         views.delete_recipe, name="deleterecipe"),
    path('recipe/update/<int:recipe_id>/',
         views.update_recipe, name="updaterecipe"),
    path('login/', views.login_view, name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('signup/', views.register_view, name='register_page'),
]
