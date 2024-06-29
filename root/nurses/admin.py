from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Nurse
from .forms import NurseCreationForm,NurseChangeForm

class NurseAdmin(UserAdmin):
    model = Nurse
    add_form = NurseCreationForm
    form = NurseChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff' ,'age','department','work_hours','personnel_number')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('father_name','national_ID','age', 'gender','department','work_hours','personnel_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('father_name','national_ID','age', 'gender','first_name','last_name','department','work_hours','personnel_number',)}),
    )


admin.site.register(Nurse,NurseAdmin)


