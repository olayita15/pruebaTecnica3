from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from ..models.employee import Employee
from ..forms import EmployeeForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

def Employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'Employee_list.html', {'employees': employees})

def Employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'Employee_detail.html', {'employee': employee})

def Employee_create(request):
    print(request.POST)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def Employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def Employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})