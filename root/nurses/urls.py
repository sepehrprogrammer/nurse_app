from django.urls import path
from . import views

urlpatterns = [
    path('nurseregister/',views.Nurse_SignupView.as_view(),name='nurse_signup'),
]