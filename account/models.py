from django.db import models

class Account(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    CheckedIn = models.BooleanField(default=False)
    Balance = models.IntegerField()