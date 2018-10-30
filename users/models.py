from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.email

    name = models.CharField(max_length=100, blank=False)
    pontos = models.IntegerField(default=0)