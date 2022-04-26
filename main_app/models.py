import datetime

from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=75)
    breed = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    age = models.DecimalField(max_digits = 4, decimal_places = 1)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    condition_choices = [
        ('NW', 'new'),
        ('LN', 'like new'),
        ('UD', 'used'),
        ('AW', 'awful')
    ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'toy_id': self.id})