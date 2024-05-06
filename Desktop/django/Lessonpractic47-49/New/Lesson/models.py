from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=250)
    price = models.TextField(blank=True)
    year = models.DateField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)