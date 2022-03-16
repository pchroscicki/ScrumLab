from enum import Enum

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


class DayName(models.Model):  # dayname choices by 'enume' Django build-in function
    class Weekday(Enum):
        Monday = 'Poniedziałek'
        Tuesday = 'Wtorek'
        Wednesday = 'Środa'
        Thursday = 'Czwartek'
        Friday = 'Piątek'
        Saturday = 'Sobota'
        Sunday = 'Niedziela'

    name = models.CharField(choices=Weekday)
    order = models.SmallIntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=256)  # (śniadanie, obiad itp)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    order = models.ForeignKey(DayName, to_fields=['order'], from_fields=['self'], on_delete=models.CASCADE)
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
