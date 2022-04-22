import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=75)
    breed = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    age = models.DecimalField(max_digits = 4, decimal_places = 1)

    def __str__(self):
        return self.name