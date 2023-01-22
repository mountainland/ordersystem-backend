from django.contrib import admin

from .models import Order, Product, Account

admin.register(Order)
admin.register(Product)
admin.register(Account)
