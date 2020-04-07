from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    NIC = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    tp_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username}'
