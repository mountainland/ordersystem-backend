from rest_framework import serializers
from .models import Order, Product, Account
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order", "ready", "timestamp", "updated"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price", "name", "visiblity", "is_donation"]

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["Firstname", "Lastname", "Funds"]