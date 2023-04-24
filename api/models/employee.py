from django.db import models
from .office import Office

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
    email = models.EmailField()
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
