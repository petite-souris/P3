from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    TATTOIST = 'TATTOIST'
    CUSTOM = 'CUSTOM'

    ROLE_CHOICES = (
        (TATTOIST, 'Tattoist-user'),
        (CUSTOM, 'Custom-user'),
        )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
