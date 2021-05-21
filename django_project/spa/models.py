from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    master = models.CharField(max_length=30)
