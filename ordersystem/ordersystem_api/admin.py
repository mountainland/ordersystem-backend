from django.contrib import admin

from .models import Order, Product

admin.register(Order)
admin.register(Product)