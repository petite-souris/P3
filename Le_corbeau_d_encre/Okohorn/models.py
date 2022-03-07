from decimal import MAX_EMAX
from django.db import models


class test(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
