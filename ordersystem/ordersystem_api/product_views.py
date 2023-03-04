from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Product items for given requested user
        '''
        Products = Product.objects.filter(visiblity=True)
        serializer = ProductSerializer(Products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        if permissions.IsAuthenticated:
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
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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

        serializer = ProductSerializer(
            instance=Product_instance, data=data, partial=True)
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
