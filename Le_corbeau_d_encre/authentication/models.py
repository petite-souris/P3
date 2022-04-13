from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TATTOIST = 'TATTOIST'
    CUSTOMER = 'CUSTOMER'
    ROLE_CHOICES = (
        (CUSTOMER, 'Client'),
        (TATTOIST, 'Tatoueur'),
        )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    date_of_birth = models.DateField(verbose_name='Date de naissance')
    email = models.EmailField(verbose_name='Adresse email')
    gender = models.CharField(max_length=30, verbose_name='Genre')

    REQUIRED_FIELDS = ['date_of_birth', 'email', 'gender']