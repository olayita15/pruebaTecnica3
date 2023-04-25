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
    Employees = Employee.objects.all()
    return render(request, 'Employee_list.html', {'Employees': Employees})

def Employee_detail(request, pk):
    Employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'Employee_detail.html', {'Employee': Employee})

def Employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'Employee_form.html', {'form': form})

def Employee_update(request, pk):
    Employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=Employee)
        if form.is_valid():
            form.save()
            return redirect('Employee_list')
    else:
        form = EmployeeForm(instance=Employee)
    return render(request, 'Employee_form.html', {'form': form})

def Employee_delete(request, pk):
    Employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        Employee.delete()
        return redirect('Employee_list')
    return render(request, 'Employee_confirm_delete.html', {'Employee': Employee})