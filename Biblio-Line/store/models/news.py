from django.db import models
from .product import Products

class News(models.Model):
    information = models.CharField(max_length=50)
    product = models.ForeignKey(Products ,on_delete=models.CASCADE,default=1 )
    
    
    


    
