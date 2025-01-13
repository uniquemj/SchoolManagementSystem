from django.contrib import admin
from schoolapp.models import Assignments
# Register your models here.


@admin.register(Assignments)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('created_at',)
