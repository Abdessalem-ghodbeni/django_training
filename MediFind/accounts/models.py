from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('patient', 'Patient'),
        ('vendeur', 'Vendeur'),
        ('personnelSante', 'Personnel de Santé'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
