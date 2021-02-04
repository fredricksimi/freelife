from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Center(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name_of_center = models.CharField(max_length=50)
    po_box = models.CharField(max_length=50)
    telephone = models.IntegerField()
    contact_person = models.CharField(max_length=50)
    email = models.EmailField()
    physical_location = models.CharField(max_length=50)

    def __str__(self):
        return self.name_of_center

