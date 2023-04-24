from django.contrib import admin
from .models import Office
from .models import Employee

admin.site.register(Office)
admin.site.register(Employee)