from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class CreateRecipe(generics.ListCreateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [AllowAny]

class ListRecipe(generics.RetrieveAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class UpdateRecipe(generics.RetrieveUpdateAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

class DeleteRecipe(generics.DestroyAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer