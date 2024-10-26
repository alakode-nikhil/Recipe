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

class SearchRecipe(generics.ListAPIView):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.kwargs.get('name')
        return Recipes.objects.filter(name__icontains = name)