from django.shortcuts import render
from django.views.generic import CreateView
from .forms import PatientRegistrationForm
from django.urls import reverse_lazy


class PatientRegistrationView(CreateView):
    form_class = PatientRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/Patient_register.html'


