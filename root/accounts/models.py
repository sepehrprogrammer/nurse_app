from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.PositiveIntegerField(null=True, blank=True)
    national_ID = models.PositiveIntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)



