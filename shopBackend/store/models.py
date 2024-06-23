from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    def __str__(self):
        return self.title