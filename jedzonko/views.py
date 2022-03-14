from datetime import datetime

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)

class Dashboard:

    def dashboard(request):
        return HttpResponse('dashboard.html')
