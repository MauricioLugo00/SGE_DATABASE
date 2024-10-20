from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'status')
    search_fields = (
        'student__first_name', 
        'student__last_name', 
        'course__course_name',
        'course__course_code'
    )
    list_filter = ('status', 'enrollment_date', 'course')
    autocomplete_fields = ['student', 'course']
    date_hierarchy = 'enrollment_date'
    
    def get_queryset(self, request):
        # Optimiza las consultas al admin agregando los campos relacionados
        return super().get_queryset(request).select_related('student', 'course')