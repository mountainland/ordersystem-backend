from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer

class OrderListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Order items for given requested user
        '''
        Orders = Order.objects.filter(user = request.user.id)
        serializer = OrderSerializer(Orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Order with given Order data
        '''
        data = {
            'order': request.data.get('order'), 
            'ready': request.data.get('ready'), 
            'user': request.user.id
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrderDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, Order_id, user_id):
        '''
        Helper method to get the object with given Order_id, and user_id
        '''
        try:
            return Order.objects.get(id=Order_id, user = user_id)
        except Order.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, Order_id, *args, **kwargs):
        '''
        Retrieves the Order with given Order_id
        '''
        Order_instance = self.get_object(Order_id, request.user.id)
        if not Order_instance:
            return Response(
                {"res": "Object with Order id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(Order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, Order_id, *args, **kwargs):
        '''
        Updates the Order item with given Order_id if exists
        '''
        Order_instance = self.get_object(Order_id, request.user.id)
        if not Order_instance:
            return Response(
                {"res": "Object with Order id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not 'order' in request.data:
            data = {
            'ready': request.data.get('ready'),
            'user': request.user.id
        }
        
        elif request.data.get('order') == "":
            data = {
                'ready': request.data.get('ready'),
                'user': request.user.id
            }

        else:
            data = {
            'order': request.data.get('order'),
            'ready': request.data.get('ready'),
            'user': request.user.id
        }
        serializer = OrderSerializer(instance = Order_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Order_id, *args, **kwargs):
        '''
        Deletes the Order item with given Order_id if exists
        '''
        Order_instance = self.get_object(Order_id, request.user.id)
        if not Order_instance:
            return Response(
                {"res": "Object with Order id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Order_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class ProductListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Product items for given requested user
        '''
        Products = Product.objects.filter(visiblity = True)
        serializer = ProductSerializer(Products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Product with given Product data
        '''
        data = {
            'price': request.data.get('price'), 
            'name': request.data.get('name'),
            'visiblity': request.data.get('visiblity')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, Product_id):
        '''
        Helper method to get the object with given Product_id, and user_id
        '''
        try:
            return Product.objects.get(id=Product_id)
        except Product.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, Product_id, *args, **kwargs):
        '''
        Retrieves the Product with given Product_id
        '''
        Product_instance = self.get_object(Product_id)
        if not Product_instance:
            return Response(
                {"res": "Object with Product id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductSerializer(Product_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, Product_id, *args, **kwargs):
        '''
        Updates the Product item with given Product_id if exists
        '''
        Product_instance = self.get_object(Product_id)
        if not Product_instance:
            return Response(
                {"res": "Object with Product id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not 'name' in request.data and 'price' in request.data and not 'visiblity' in request.data:
            data = {
            'price': request.data.get('price')
        }

        else:
            data = {
            'name': request.data.get('name'),
            'visiblity': request.data.get('info'),
            'price': request.data.get('price')
        }
        
        serializer = ProductSerializer(instance = Product_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, Product_id, *args, **kwargs):
        '''
        Deletes the Product item with given Product_id if exists
        '''
        Product_instance = self.get_object(Product_id, request.user.id)
        if not Product_instance:
            return Response(
                {"res": "Object with Product id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        Product_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )