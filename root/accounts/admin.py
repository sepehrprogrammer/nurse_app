from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff' ,'age')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('father_name','national_ID','age', 'gender',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('father_name','national_ID','age', 'gender','first_name','last_name',)}),
    )



admin.site.register(CustomUser, CustomUserAdmin)

