import random
from datetime import datetime

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)   # zmiana z test.html

class CarouselView(View):
    def get(self, request):
        recipe = Recipe.objects.all()
        random.shuffle(recipe)
        recipes = recipe[0:2]
        return render(request, 'index.html', context={'recipes': recipes})

