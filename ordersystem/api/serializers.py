from rest_framework import serializers


from ordersystem_api.models import Product

from ordersystem_api.models import Order



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

