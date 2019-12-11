from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    age=models.IntegerField()

#用户表
class User(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=20)