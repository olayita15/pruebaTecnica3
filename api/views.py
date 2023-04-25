from django.http import HttpResponse
from django.shortcuts import render

from .Views.employee_views import *
from .Views.office_views import *

def base(request):
    offices = Office.objects.all()
    employees = Employee.objects.all()
    return render(request,'base.html', {'offices':offices, 'employees':employees})
