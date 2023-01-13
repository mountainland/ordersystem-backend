from django.db import models

from django.contrib.auth.models import User

import json

class Order(models.Model):
    order = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    ready = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return json.loads(self.order)

class Product(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    visiblity = models.BooleanField(default = True)

    def __str__(self):
        return json.loads(self.name)