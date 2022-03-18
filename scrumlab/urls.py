"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from jedzonko.models import Recipe
from jedzonko.views import IndexView, PulpitView, ModyfikujPlanView, PlanyView, \
    PrzepisyView, DodajPrzepisView, DodajPlanView, DodajPrzepisDoPlanuView, \
    DetalePrzepisuView, DetalePlanuView, ModyfikujPrzepisView
from django.contrib import admin
from django.urls import path, re_path



urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', IndexView.as_view()),
    path('recipe/list', Recipe),

    path('', IndexView.as_view()),
    path('main/', PulpitView.as_view()),
    path('recipe/add/', DodajPrzepisView.as_view()),
    path('recipe/list/', PrzepisyView.as_view()),
    path('plan/add/', DodajPlanView.as_view()),
    path('plan/list/', PlanyView.as_view()),
    path('plan/modify/<int:id>/', ModyfikujPlanView.as_view()),
    path('plan/add/recipe/', DodajPrzepisDoPlanuView.as_view()),
    path('recipe/<int:id>/', DetalePrzepisuView.as_view()),
    path('plan/<int:id>', DetalePlanuView.as_view()),
    path('recipe/modify/<int:id>', ModyfikujPrzepisView.as_view()),
    path('plan/<int:id>/', DetalePlanuView.as_view()),
]
