from django import forms
from .models import Communication

class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = ('patient', 'status')