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
        schedules_number = Schedule.objects.count()
        recipes_number = Recipe.objects.count()
        ctx = {"actual_date": datetime.now(), 'schedules_number': schedules_number, 'recipes_number': recipes_number, 'recipes':recipes}
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
    def post(self, request):
        planName = request.POST['planName']
        planDescription = request.POST['planDescription']
        Schedule.objects.create(name="planName", description="planDescription")
        return render(request, 'app-add-schedules.html')  # HttpResponse("Dodano plan!")


class DodajPrzepisDoPlanuView(View):
    def get(self, request):
        return render(request, 'app-details-schedules.html')


class DetalePrzepisuView(View):
    def get(self, request):
        return render(request, 'app-recipe-details.html')
