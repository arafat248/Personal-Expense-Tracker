from django.db import models
from django.contrib.auth.models import User
from Category.models import CategoryModel

# Create your models here.
class TansactionModel(models.Model):
    type_choice =[
        ('income', 'Income'),
        ('expense', 'Expense')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    types = models.CharField(max_length=50, choices= type_choice)
    date = models.DateField(auto_now_add=False)
    note = models.TextField()
    created_at = models.DateField(auto_now_add=False)