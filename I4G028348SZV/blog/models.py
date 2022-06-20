from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.CharField
    Author=models.ForiegnKey(User, on_delete=models.CASCADE)
    Created_Date=models.DateTimeField
    Published_Date=models.DateTimeField