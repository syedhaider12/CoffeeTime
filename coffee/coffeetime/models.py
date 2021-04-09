from django.db import models

# Create your models here.
class coffee(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='pics')

class tea(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='pics')

class juice (models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='pics')

class contact(models.Model):
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    query=models.TextField()

