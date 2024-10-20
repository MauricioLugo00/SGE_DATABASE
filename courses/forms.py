from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'description', 'teacher', 'credits']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }