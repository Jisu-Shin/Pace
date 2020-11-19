from django.db import models

class Custom(models.Model):
    message=models.CharField(max_length=100)

class Store(models.Model):
    message=models.CharField(max_length=100)

