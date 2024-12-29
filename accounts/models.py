from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Teacher(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    school_id = models.CharField(max_length=100, default="0", null=True)

class Student(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    roll_number = models.CharField(max_length=4, default = "0")