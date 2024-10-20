from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'status']
        
    def clean(self):
        cleaned_data = super().clean()
        student = cleaned_data.get('student')
        course = cleaned_data.get('course')
        
        # Verificar si ya existe una matrícula activa para este estudiante y curso
        if student and course:
            exists = Enrollment.objects.filter(
                student=student,
                course=course,
                status='active'
            ).exists()
            if exists:
                raise forms.ValidationError(
                    "Este estudiante ya está matriculado en este curso."
                )
        return cleaned_data

class EnrollmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['status']