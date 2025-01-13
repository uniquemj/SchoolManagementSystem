from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
from accounts.models import CustomUser, Teacher, Student

@receiver(post_save, sender = CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.is_teacher == True:
        teacher_count = Teacher.objects.all().count()

        Teacher.objects.create(
            user = instance,
            name = f'{instance.first_name} {instance.last_name}',
            school_id = f'{teacher_count + 1}'
        )

@receiver(post_save, sender = CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.is_student == True:

        Student.objects.create(
            user = instance,
            name = f'{instance.first_name} {instance.last_name}'
        )