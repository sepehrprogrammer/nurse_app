from django.db import models
from accounts.models import CustomUser


class Patient(CustomUser):
    medical_history = models.TextField()
    current_conditions = models.TextField()
    allergies = models.TextField(null=True, blank=True)
    medications = models.TextField()
    location = models.CharField(max_length=100)
    illness_type = models.CharField(max_length=100)
    illness_name = models.CharField(max_length=100)
    blood_pressure = models.IntegerField(null=True, blank=True)
    blood_sugar = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    addiction = models.BooleanField(null=True, blank=True)
    addiction_name = models.CharField(null=True, blank=True, max_length=100)







