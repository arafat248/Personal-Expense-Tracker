from django.shortcuts import render
from rest_framework import viewsets
from .models import CategoryModel
from .serializer import Category_Serial

# Create your views here.
class CateloryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = Category_Serial