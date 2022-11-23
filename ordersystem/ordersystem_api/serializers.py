from rest_framework import serializers
from .models import Order, Product
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order", "ready", "timestamp", "updated", "user"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price", "name", "info"]