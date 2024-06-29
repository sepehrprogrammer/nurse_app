from django.shortcuts import render
from django.views.generic import CreateView
from .forms import NurseCreationForm
from django.urls import reverse_lazy

class Nurse_SignupView(CreateView):
    form_class = NurseCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/Nurse_register.html'


