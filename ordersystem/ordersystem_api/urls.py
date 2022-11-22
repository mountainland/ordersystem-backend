from django.urls import path, include
from .views import (
    OrderListApiView,
    OrderDetailApiView,
    ProductListApiView,
    ProductDetailApiView,

)

urlpatterns = [
    path('api', OrderListApiView.as_view()),
    path('api/<int:Order_id>/', OrderDetailApiView.as_view()),
    path('api/products/', ProductListApiView.as_view()),
    path('api/product/<int:Product_id>', ProductDetailApiView.as_view())
]