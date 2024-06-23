from django.contrib import admin
from .models import Cart, OrderItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(OrderItem)