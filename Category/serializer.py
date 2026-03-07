from rest_framework import serializers
from .models import CategoryModel

class Category_Serial(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id', 'user', 'name', 'category_at',
        ]