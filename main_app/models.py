from datetime import date
from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils import timezone

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        )
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    NEW = 'new'
    LIKENEW = 'like new'
    USED = 'used'
    AWFUL = 'awful'
    conditions = [
        (NEW, 'new'),
        (LIKENEW, 'like new'),
        (USED, 'used'),
        (AWFUL, 'awful')
    ]
    status = models.CharField(
        max_length=10,
        choices=conditions,
        default=NEW,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})