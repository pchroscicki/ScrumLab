import random
from datetime import datetime
from django.shortcuts import render
from django.views import View
from jedzonko.models import Schedule, Recipe


class IndexView(View):
    def get(self, request):
        recipe = list(Recipe.objects.all())
        random.shuffle(recipe)
        recipes = recipe[0:3]
        ctx = {"actual_date": datetime.now(), "recipes": recipes}
        return render(request, "index.html", ctx)   # zmiana z test.html


class PrzepisyView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')


class PlanyView(View):
    def get(self, request):
        return render(request, 'app-schedules.html')

class PulpitView(View):
    def get(self, request):
        return render(request, 'dashboard.html') 


class ZaplanujJedzonkoView(View):
    def get(self, request):
        return render(request, 'index.html')


class DodajPrzepisView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')


class ModyfikujPrzepisView(View):
    def get(self, request):
        return render(request, 'app-edit-recipe.html')


class ModyfikujPlanView(View):
    def get(self, request):
        return render(request, 'app-edit-schedules.html')


class DodajPlanView(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')


class DodajPrzepisDoPlanuView(View):
    def get(self, request):
        return render(request, 'app-details-schedules.html')

      
class LiczbaPlanow(View):
    def get(self, request):
        number = Schedule.objects.count()
        return render(request, 'index.html', {'number': number})


class DetalePrzepisuView(View):
    def get(self, request):
        return render(request, 'app-recipe-details.html')
