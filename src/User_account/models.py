from django.contrib.auth.models import AbstractUser
from django.db import models


class myUser(AbstractUser ):
    is_tenant = models.BooleanField('tenant status', default=False)
    is_landlord = models.BooleanField('landlord status', default=False)
    id_number = models.CharField(max_length=20)
    Phone_number = models.CharField(max_length=10)
    #birth_date = models.DateField(default=2000/01/10)
    profile_image=models.ImageField(upload_to='images/',default='image')
    id_copy = models.FileField(upload_to='documents/', default='document')
    