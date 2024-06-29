from django.db import models
from accounts.models import CustomUser


class Nurse(CustomUser):
    personnel_number = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    work_hours = models.CharField(max_length=50)


