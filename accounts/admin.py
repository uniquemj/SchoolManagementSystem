from django.contrib import admin
from accounts.models import Classroom, CustomUser, Teacher, Student
# Register your models here.

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    ordering= ('classroom_number',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'school_id',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number','classroom')