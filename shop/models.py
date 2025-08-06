from django.db import models

# Create your models here.
   
class Post(models.Model):
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)