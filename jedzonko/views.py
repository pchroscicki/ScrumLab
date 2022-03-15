from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)   # zmiana z test.html


class PrzepisyView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')


class PlanyView(View):
    def get(self, request):
        return render(request, 'app-schedules.html')

class PulpitView(View):
    def dashboard(self, request):
        return render(request, 'dashboard.html') 


class ZaplanujJedzonkoView(View):
    def LandingPage(self, request):
        return render(request, 'index.html')


class DodajPrzepisView(View):
    def AddRecipe(self, request):
        return render(request, 'app-add-recipe.html')


class ModyfikujPrzepisView(View):
    def ModifyRecipe(self, request):
        return render(request, 'app-edit-recipe.html')


class ModyfikujPlanView(View):
    def ModifySchedule(self, request):
        return render(request, 'app-edit-schedules.html')


class DodajPlanView(View):
    def AddSchedule(self, request):
        return render(request, 'app-add-schedules.html')


class DodajPrzepisDoPlanuView(View):
    def AddRecipeToSchedule(self, request):
        return render(request, 'app-details-schedules')
