from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'specialization')
    search_fields = ('first_name', 'last_name', 'email', 'specialization')
    list_filter = ('specialization', 'created_at')
    ordering = ('last_name', 'first_name')