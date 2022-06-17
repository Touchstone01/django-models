from django.db import models
from operator import mod
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    Title = models.CharField(max_length=200,blank=False)
    Text = models.TextField(blank=False)
    Author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField() 
    published_date = models.DateTimeField() 