from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'teacher', 'credits')
    search_fields = ('course_name', 'course_code', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('credits', 'teacher', 'created_at')
    ordering = ('course_code',)
    autocomplete_fields = ['teacher']