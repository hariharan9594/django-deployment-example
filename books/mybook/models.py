from django.db import models

# Create your models
class Booksinfo(models.Model):
    Name  = models.CharField(max_length=30)
    Author = models.CharField(max_length=20)
    #date = models.DateField()
    quantity = models.IntegerField()

