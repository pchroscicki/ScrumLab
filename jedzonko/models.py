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
    preparation = models.TextField(null=True)
    votes = models.IntegerField(default=0)


class Schedule(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    created = models.DateTimeField(default=datetime.date.today)
    updated = models.DateTimeField(default=datetime.date.today)






