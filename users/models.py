from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
