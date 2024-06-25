from django.db import models

# Create your models here.

class StoreItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    def __str__(self):
        return self.title