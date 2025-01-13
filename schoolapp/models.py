from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Teacher, Student, Classroom
# Create your models here.



class Assignments(models.Model):
    uploaded_by = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    upload_to = models.ForeignKey(Classroom, on_delete = models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    assignment_field = models.FileField(upload_to="assignments/", null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)