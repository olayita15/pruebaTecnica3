from django.db import models

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
