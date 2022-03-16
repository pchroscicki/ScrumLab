import random
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
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
        schedule_list = list(Schedule.objects.all().order_by('-created'))
        last_schedule = schedule_list[0]
        ctx = {"actual_date": datetime.now(), 'schedules_number': schedules_number, 'recipes_number': recipes_number, 'recipes':recipes, 'last_schedule': last_schedule}
        return render(request, "index.html", ctx)   # zmiana z test.html



class PrzepisyView(View):
    def get(self, request):
        recipe_list = Recipe.objects.all().order_by('votes')
        paginator = Paginator(recipe_list, 50)  # Show 50 recipes per page

        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        ctx = {'recipes': recipes, 'recipe_list': recipe_list}
        return render(request, 'app-recipes.html', ctx)


class PlanyView(View):
    def get(self, request):
        return render(request, 'app-schedules.html')

class PulpitView(View):
    def get(self, request):
        return render(request, 'dashboard.html') 


class ZaplanujJedzonkoView(View):
    def get(self, request):
        return render(request, '')


class DodajPrzepisView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')
    def post(self, request):
        recipe = request.POST['recipe']
        description = request.POST['description']
        time = int(request.POST['time'])
        preparation = request.POST['preparation']
        ingredients = request.POST['ingredients']
        Recipe.objects.create(name=recipe, ingredients=ingredients, description=description, preparation_time=time, preparation=preparation)
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


class DetalePrzepisuView(View):
    def get(self, request):
        # recipes = list(Recipe.objects.all())
        return render(request, 'app-recipe-details.html')

