from datetime import datetime

from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "index.html", ctx)   # zmiana z test.html


class RecipeView(View):
    def get(self, request):
        return render(request, 'app-recipes.html')


class Dashboard(View):
    def dashboard(self, request):
        return render(request, 'dashboard.html') 

