from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Classroom(models.Model):
    classroom_number = models.CharField(max_length=3, default="1")

    def __str__(self):
        return f'{self.classroom_number}'

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    school_id = models.CharField(max_length=100, default="0", null=True)
    classrooms  = models.ManyToManyField(Classroom)

    def __str__(self):
        return f'{self.name}'
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    name = models.CharField(max_length=150, null=True, blank=True)
    roll_number = models.CharField(max_length=4, default = "0")
    classroom = models.ForeignKey(Classroom, on_delete= models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'