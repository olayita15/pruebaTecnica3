from django.urls import path

from .Views import *
from .Views.office_views import (
    OfficeListView,
    OfficeDetailView,
    office_list,
    office_detail,
    office_create,
    office_update,
    office_delete,
)
from .Views.employee_views import (
    EmployeeListView,
    EmployeeDetailView,
    Employee_create,
    Employee_update,
    Employee_delete,
)

urlpatterns = [
    
    path('offices/', office_list_view, name='office_list'),
    path('offices/<int:pk>/', office_detail_view, name='office_detail'),
    path('', OfficeListView.as_view(), name='office_list_cbv'),
    path('<int:pk>/', OfficeDetailView.as_view(), name='office_detail_cbv'),
    path('create/', office_create, name='office_create'),
    path('<int:pk>/update/', office_update, name='office_update'),
    path('<int:pk>/delete/', office_delete, name='office_delete'),
    path('list/', office_list, name='office_list_fbv'),
    path('detail/<int:pk>/', office_detail, name='office_detail_fbv'),

    path('employees/', employee_list_view, name='employee_list'),
    path('employees/<int:pk>/', employee_detail_view, name='employee_detail'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', Employee_create, name='employee_create'),
    path('employees/update/<int:pk>/', Employee_update, name='employee_update'),
    path('employees/delete/<int:pk>/', Employee_delete, name='employee_delete'),
]

