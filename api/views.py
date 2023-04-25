from django.http import HttpResponse
from django.shortcuts import render

from .views.employee_views import *
from .views.office_views import *

def home(request):
    return HttpResponse("<h1>Hola Mundo</h1>")
