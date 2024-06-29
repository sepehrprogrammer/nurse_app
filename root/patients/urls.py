from django.urls import path
from . import views


urlpatterns = [
    path('patientregister/', views.PatientRegistrationView.as_view(), name='patient_signup'),
]