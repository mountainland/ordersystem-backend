from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("products/((?P<pk>\d+)/)?", csrf_exempt(ProductView.as_view())),
	re_path("orders/((?P<pk>\d+)/)?", csrf_exempt(OrderView.as_view())),
	re_path("account/((?P<pk>\d+)/)?", csrf_exempt(AccountView.as_view())),

]