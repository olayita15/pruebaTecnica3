# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.generic import ListView, DetailView
# from ..models.office import Office
# from ..forms import OfficeForm

# class OfficeListView(ListView):
#     model = Office
#     template_name = 'office_list.html'
#     context_object_name = 'offices'

# class OfficeDetailView(DetailView):
#     model = Office
#     template_name = 'office_detail.html'
#     context_object_name = 'office'

# def office_list(request):
#     offices = Office.objects.all()
#     return render(request, 'office_list.html', {'offices': offices})

# def office_detail(request, pk):
#     office = get_object_or_404(Office, pk=pk)
#     return render(request, 'office_detail.html', {'office': office})

# def office_create(request):
#     if request.method == 'POST':
#         form = OfficeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('office_list')
#     else:
#         form = OfficeForm()
#     return render(request, 'office_form.html', {'form': form})

# def office_update(request, pk):
#     office = get_object_or_404(Office, pk=pk)
#     if request.method == 'POST':
#         form = OfficeForm(request.POST, instance=office)
#         if form.is_valid():
#             form.save()
#             return redirect('office_list')
#     else:
#         form = OfficeForm(instance=office)
#     return render(request, 'office_form.html', {'form': form})

# def office_delete(request, pk):
#     office = get_object_or_404(Office, pk=pk)
#     if request.method == 'POST':
#         office.delete()
#         return redirect('office_list')
#     return render(request, 'office_confirm_delete.html', {'office': office})