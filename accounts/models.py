from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User Model
    """

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
