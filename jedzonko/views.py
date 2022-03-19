import random
from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Schedule, Recipe, DayName, RecipePlan
from django.http import Http404
from jedzonko.models import Schedule, Recipe, RecipePlan, Page


class IndexView(View):
    def get(self, request):
        recipe = list(Recipe.objects.all())
        random.shuffle(recipe)
        recipes = recipe[0:3]
        ctx = {"actual_date": datetime.now(), 'recipes': recipes}
        return render(request, "index.html", ctx)   # zmiana z test.html
    def post(self, request):
        search = request.POST['search']
        search_recipe = Recipe.objects.get(name=search)
        return redirect(f'/recipe/{search_recipe.id}')


class PrzepisyView(View):
    def get(self, request):
        recipe_list = list(Recipe.objects.all().order_by('-votes', '-created'))
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
        plans = list(Schedule.objects.all())
        recipes = list(Recipe.objects.all())
        return render(request, 'app-schedules-meal-recipe.html', {'plans': plans, 'recipes': recipes})
    def post(self, request):
        food = request.POST['foodname']
        number = request.POST['number']
        id_plan = request.POST['plan']
        id_recipe = request.POST['recipe']
        id_day = request.POST['day']
        if not food and number and id_plan and id_recipe and id_day:
            text = 'Wypełnij wszystkie pola'
            return render(request, 'app-schedules-meal-recipe.html', {'text': text})

        # musimy przekierować użytkownika na stronę `/plan/<id>/` gdzie <id> to id wybranego planu - a nie nowego RecipePlan
        # wyciągamy id z powyższych danych żeby dodać je RecipePlan - tabele powiązane przez ID
        recipe = Recipe.objects.get(id=id_recipe)
        schedule = Schedule.objects.get(id=id_plan)
        day = DayName.objects.get(name=id_day)
        RecipePlan.objects.create(meal_name=food, recipe=recipe, schedule=schedule, order=number, day_name=day)
        return redirect(f'/plan/{schedule.id}')

class DetalePrzepisuView(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        ctx = {'recipe': recipe}
        return render(request, 'app-recipe-details.html', ctx)

    def post(self, request, id):
        recipe = Recipe.objects.get(pk=id)
        if 'Like' in request.POST:
            recipe.votes += 1
        elif 'Hate' in request.POST:
            recipe.votes -= 1
        recipe.save()
        ctx = {'recipe': recipe}
        return render(request, 'app-recipe-details.html', ctx)

class DetalePlanuView(View):
    def get(self, request, id):
        plan = Schedule.objects.get(pk=id)
        recipeplan = RecipePlan.objects.all()
        ctx = {'plan': plan, 'recipeplan': recipeplan}
        return render(request, 'app-details-schedules.html', ctx)


class ModyfikujPrzepisView(View):
    def get(self, request, id):
        try:
            recipe = Recipe.objects.get(pk=id)
        except Recipe.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'app-modify-recipe.html', {'recipe': recipe})
    def post(self, request, id):
        new_recipe = request.POST['recipe']
        new_description = request.POST['description']
        new_preparation_time = request.POST['time']
        new_preparation = request.POST['preparation']
        new_ingredients = request.POST['ingredients']
        if not new_recipe or new_description or new_preparation_time or new_ingredients:
            text = 'Uzupełnij wszystkie pola'
            return render(request, 'app-modify-recipe.html', {'text': text})
        Recipe.objects.create(name=new_recipe, ingredients=new_ingredients, description=new_description, preparation_time=new_preparation_time, preparation=new_preparation)
        modified_recipe = Recipe.objects.create(name=new_recipe, ingredients=new_ingredients, description=new_description, preparation_time=new_preparation_time, preparation=new_preparation)
        return redirect(f'/recipe/modify/{modified_recipe.id}')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

# class AboutView(View):
#     def get(self, request, slug):
#         try:
#             slug = Page.objects.get(slug)
#         except Page.DoesNotExist:
#             raise Http404("Page does not exist")
#         return render(request, 'about.html', {'slug': slug})
