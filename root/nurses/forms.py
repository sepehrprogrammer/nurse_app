from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Nurse

class NurseCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Nurse
        fields = UserCreationForm.Meta.fields + (
        "age", "father_name", "national_ID", "first_name", "last_name", "gender","department","work_hours","personnel_number")


class NurseChangeForm(UserChangeForm):
    class Meta:
        model = Nurse
        fields = UserChangeForm.Meta.fields
