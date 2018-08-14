from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

