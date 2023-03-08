from django.db import models

import json



class Product(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    is_public = models.BooleanField(default = True)

    def __str__(self):
        return json.loads(self.name)