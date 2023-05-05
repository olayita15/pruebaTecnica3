from rest_framework import generics
from ...models import Office
from ...serializers.office_serializer import OfficeSerializer

class OfficeListCreateView(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class OfficeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
