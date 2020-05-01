from django.urls import path
from recipe.views import index

urlpatterns = [
     path('', index, name='index'),
]
