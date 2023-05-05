# from django.http import HttpResponse
# from django.shortcuts import render
from .models import Office, Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# from .Views.employee_views import *
# from .Views.office_views import *
from .Views.api.employee_views_api import *
from .Views.api.office_views_api import *

# def base(request):
#     offices = Office.objects.all()
#     employees = Employee.objects.all()
#     return render(request,'base.html', {'offices':offices, 'employees':employees})

@api_view(['GET'])
def base(request):
    office = Office.objects.all()
    employee = Employee.objects.all()

    office_serializer = OfficeSerializer(office, many=True)
    employee_serializer = EmployeeSerializer(employee, many=True)

    data = {
        'sedes': office_serializer.data,
        'empleados': employee_serializer.data
    }

    return Response(data, status=status.HTTP_200_OK)


