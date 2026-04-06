from rest_framework import serializers
from .models import TansactionModel, CategoryModel
from django.contrib.auth.models import User

class Transcation_Serial(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'     
    )
    category = serializers.SlugRelatedField(
        queryset=CategoryModel.objects.all(),
        slug_field='category_name'
    )
    class Meta:
        model = TansactionModel
        fields = ['id', 'user', 'category', 'types', 'amount', 'note', 'date', 'created_at']