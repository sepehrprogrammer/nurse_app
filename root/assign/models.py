from django.db import models
from nurses.models import Nurse
from patients.models import Patient
from django.conf import settings

class Communication(models.Model):
    """
    Model to manage the relationships between Nurses and Patients
    and store their communication history.
    """

    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='nurse_communications',
        limit_choices_to={'groups__name': 'Nurses'}
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_communications',
        limit_choices_to={'groups__name': 'Patients'}
    )
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_communications',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive')
        ],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Communication between {self.nurse} and {self.patient}'
