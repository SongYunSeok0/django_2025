from django.db import models

# Create your models here.
   
class Main(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)

class Outer(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)

class Top(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)

class Bottom(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)

class Shoes(models.Model):
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=3)   