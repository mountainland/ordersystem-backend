from django.db import models

from django.contrib.auth.models import User

import json

class Order(models.Model):
    order = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    ready = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return json.loads(self.order)