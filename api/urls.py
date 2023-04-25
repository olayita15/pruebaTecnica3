from django.urls import path

from .views import home
from .views import *


urlpatterns = [
    path('offices/', office_list_view, name='office_list'),
    path('offices/<int:pk>/', office_detail_view, name='office_detail'),

    path('employees/', employee_list_view, name='employee_list'),
    path('employees/<int:pk>/', employee_detail_view, name='employee_detail'),
]

