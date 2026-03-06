from rest_framework import serializers
from .models import TansactionModel

class Transcation_Serial(serializers.ModelSerializer):
    class Meta:
        model : TansactionModel
        fields = "__all__"