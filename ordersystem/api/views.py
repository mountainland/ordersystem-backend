from http import HTTPStatus
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from api.serializers import *


from ordersystem_api.models import Product

from ordersystem_api.models import Order



class ProductView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ProductSerializer(data=request.POST)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Created.',
            'success': True
        }, status=HTTPStatus.OK)

    def get(self, request, pk=None):
        if not pk:
            return Response({
                'data': [ProductSerializer(instance=obj).data for obj in Product.objects.all()],
                'success': True
            }, status=HTTPStatus.OK)
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        return Response({
            'data': ProductSerializer(instance=obj).data,
            'success': True
        }, status=HTTPStatus.OK)

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        serializer = ProductSerializer(instance=obj, data=request.POST, partial=True)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Updated.',
            'success': True
        }, status=HTTPStatus.OK)

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Product, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=HTTPStatus.OK)


class OrderView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = OrderSerializer(data=request.POST)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Created.',
            'success': True
        }, status=HTTPStatus.OK)

    def get(self, request, pk=None):
        if not pk:
            return Response({
                'data': [OrderSerializer(instance=obj).data for obj in Order.objects.all()],
                'success': True
            }, status=HTTPStatus.OK)
        try:
            obj = get_object_or_404(Order, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        return Response({
            'data': OrderSerializer(instance=obj).data,
            'success': True
        }, status=HTTPStatus.OK)

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Order, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        serializer = OrderSerializer(instance=obj, data=request.POST, partial=True)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        serializer.save()
        return Response(data={
            'message': 'Record Updated.',
            'success': True
        }, status=HTTPStatus.OK)

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Order, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=HTTPStatus.OK)

