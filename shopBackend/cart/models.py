from django.db import models
from django.conf import settings
from store.models import Item

# Create your models here.



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
        return self.item
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
