from django.contrib import admin
from .models import Office
from .models import Employee

@admin.register(Office)
class officeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'city')
    list_filter = ['city',]
    
@admin.register(Employee)
class employeeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'office')
    list_filter = ['office',]