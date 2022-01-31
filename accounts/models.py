from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.

# extending user model to make it easy later to add custome fields to user table
class User(AbstractUser):
    account_type_choices = (
        ('BASIC', 'basic'),
        ('PREMIUM','premium'),
    )
    account_type = models.CharField(max_length=10, choices=account_type_choices, default='BASIC')