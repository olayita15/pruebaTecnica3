from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models.office import Office

class OfficeListView(ListView):
    model = Office
    template_name = 'office_list.html'
    context_object_name = 'offices'

class OfficeDetailView(DetailView):
    model = Office
    template_name = 'office_detail.html'
    context_object_name = 'office'
