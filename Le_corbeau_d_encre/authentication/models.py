from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    PREMIUM = 'PREMIUM'
    FREE = 'FREE'

    ROLE_CHOICES = (
        (PREMIUM, 'Premium-user'),
        (FREE, 'Free-user'),
        )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
