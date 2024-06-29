from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Patient

class PatientRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Patient
        fields = UserCreationForm.Meta.fields + ("age","father_name","national_ID","first_name","last_name","gender",
                                                 "medical_history","medications",)

class PatientUpdateForm(UserChangeForm):
    class Meta:
        model = Patient
        fields = UserChangeForm.Meta.fields


