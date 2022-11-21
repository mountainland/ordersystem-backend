from django.urls import path, include
from .views import (
    OrderListApiView,
    TodoDetailApiView
)

urlpatterns = [
    path('api', OrderListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]