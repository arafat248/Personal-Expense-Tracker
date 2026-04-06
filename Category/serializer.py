from rest_framework import serializers
from .models import CategoryModel

class Category_Serial(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id', 'user', 'category_name', 'created_at',
        ]