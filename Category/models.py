from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)
    created_at  = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.category_name
    