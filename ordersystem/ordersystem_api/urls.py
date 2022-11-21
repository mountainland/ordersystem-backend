from django.urls import path, include
from .views import (
    OrderListApiView,
)

urlpatterns = [
    path('api', OrderListApiView.as_view()),
]