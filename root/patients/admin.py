from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Patient
from .forms import PatientRegistrationForm,PatientUpdateForm


class PatientAdmin(UserAdmin):
    add_form = PatientRegistrationForm
    form = PatientUpdateForm
    model = Patient
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'age','medications','weight','height','medical_history','current_conditions','blood_pressure','blood_sugar','location')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('father_name', 'national_ID', 'age', 'gender','medications','weight','height','medical_history','current_conditions','blood_pressure','blood_sugar','location',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('father_name', 'national_ID', 'age', 'gender', 'first_name', 'last_name','medications','weight','height','medical_history','current_conditions','blood_pressure','blood_sugar','location',)}),
    )


admin.site.register(Patient, PatientAdmin)
