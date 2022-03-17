import random
from datetime import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Schedule, Recipe


class IndexView(View):
    def get(self, request):
        recipe = list(Recipe.objects.all())
        random.shuffle(recipe)
        recipes = recipe[0:3]
        ctx = {"actual_date": datetime.now(), 'recipes': recipes}
        return render(request, "index.html", ctx)   # zmiana z test.html



class PrzepisyView(View):
    def get(self, request):
        recipe_list = list(Recipe.objects.all().order_by('votes', 'created'))
        paginator = Paginator(recipe_list, 50)  # Show 50 recipes per page
        page = request.GET.get('page')
        recipes = paginator.get_page(page)
        ctx = {'recipes': recipes, 'recipe_list': recipe_list}
        return render(request, 'app-recipes.html', ctx)


class PlanyView(View):
    def get(self, request):
        schedule_list = list(Schedule.objects.all().order_by('name'))
        paginator = Paginator(schedule_list, 50)
        page = request.GET.get('page')
        schedules = paginator.get_page(page)
        ctx = {'schedules': schedules, 'schedule_list': schedule_list}
        return render(request, 'app-schedules.html', ctx)

class PulpitView(View):
    def get(self, request):
        schedules_number = Schedule.objects.count()
        recipes_number = Recipe.objects.count()
        schedule_list = list(Schedule.objects.all().order_by('-created'))
        last_schedule = schedule_list[0]
        ctx = {'schedules_number': schedules_number, 'recipes_number': recipes_number, 'last_schedule': last_schedule}
        return render(request, 'dashboard.html', ctx)


class ZaplanujJedzonkoView(View):
    def get(self, request):
        return render(request, '')


class DodajPrzepisView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')
    def post(self, request):
        recipe = request.POST['recipe']
        description = request.POST['description']
        time = (request.POST['time'])
        preparation = request.POST['preparation']
        ingredients = request.POST['ingredients']
        if not (recipe and description and time and preparation and ingredients):
            text = 'Wypełnij poprawnie wszystkie pola'
            return render(request, 'app-add-recipe.html', {'text': text})
        Recipe.objects.create(name=recipe, ingredients=ingredients, description=description, preparation_time=time,
                              preparation=preparation)
        return redirect('/recipe/list/')

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
        planname = request.POST['planName']
        plandescription = request.POST['planDescription']
        if not planname or not plandescription:
            text = 'Wypełnij wszystkie pola'
            return render(request, 'app-add-schedules.html', {'text': text})
        Schedule.objects.create(name=planname, description=plandescription)
        return redirect('/plan/list/')


class DodajPrzepisDoPlanuView(View):
    def get(self, request):
        return render(request, 'app-schedules-meal-recipe.html')

class DetalePrzepisuView(View):
    def get(self, request, id):
        #recipes = list(Recipe.objects.all()) ### Czy to komuś jest tutaj potrzebne? (PCh)
        recipe = Recipe.objects.get(pk=id)
        ctx = {'recipe': recipe}
        return render(request, 'app-recipe-details.html', ctx)

class DetalePlanuView(View):
    def get(self, request, id):
        schedule = Schedule.objects.get(pk=id)
        return render(request, 'app-details-schedules.html', context={'schedule': schedule})