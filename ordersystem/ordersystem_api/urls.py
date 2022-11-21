from django.urls import path, include
from .views import (
    OrderListApiView,
    OrderDetailApiView
)

urlpatterns = [
    path('api', OrderListApiView.as_view()),
    path('api/<int:Order_id>/', OrderDetailApiView.as_view()),
]