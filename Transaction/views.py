from django.shortcuts import render
from rest_framework import viewsets
from .models import TansactionModel
from .serializer import Transcation_Serial


# Create your views here.
class TransactionView(viewsets.ModelViewSet):
    queryset = TansactionModel.objects.all()
    serializer_class = Transcation_Serial
    