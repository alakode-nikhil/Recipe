from django.urls import path
from .views import *

urlpatterns = [
    path('create-recipe/', CreateRecipe.as_view(), name='create-recipe'),
    path('list-recipe/<int:pk>/', ListRecipe.as_view(), name='list-recipe'),
    path('update-recipe/<int:pk>/', UpdateRecipe.as_view(), name='update-recipe'),
    path('delete-recipe/<int:pk>/', DeleteRecipe.as_view(), name='delete-recipe'),
    path('search-recipe/<str:name>/', SearchRecipe.as_view(), name='search_recipe'),
]