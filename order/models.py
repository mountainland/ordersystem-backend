from django.db import models

import json

class Order(models.Model):
    order = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    ready = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    customer = models.CharField(max_length=50)

    def __str__(self):
        return json.loads(self.order)