from django.db import models
import datetime


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.date.today)
    updated = models.DateTimeField(default=datetime.date.today)
    preparation_time = models.IntegerField(null=True)
    votes = models.IntegerField(default=0)


class Schedule(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.date.today)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')


CHOICES = (
    ('Mon', 'Poniedziałek'),
    ('Tue', 'Wtorek'),
    ('Wed', 'Środa'),
    ('Thu', 'Czwartek'),
    ('Fri', 'Piątek'),
    ('Sat', 'Sobota'),
    ('Sun', 'Niedziela')
)


class DayName(models.Model):
    name = models.CharField(max_length=64, choices=CHOICES)
    order = models.SmallIntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=256)  # (śniadanie, obiad itp)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    order = models.ForeignKey(DayName, on_delete=models.CASCADE, related_name='order_id')
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
