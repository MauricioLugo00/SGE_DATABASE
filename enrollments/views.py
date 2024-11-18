from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Subquery, OuterRef
from .models import Enrollment
from .forms import EnrollmentForm, EnrollmentUpdateForm

# Listado de matrículas con agrupación por curso
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrupación: Total de matrículas por curso
        context['enrollments_by_course'] = Enrollment.objects.values(
            'course__course_name'
        ).annotate(total=Count('id'))
        return context

# Crear matrícula
class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

# Actualizar matrícula
class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentUpdateForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

# Eliminar matrícula
class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollments/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment-list')

# Reporte: Estudiantes matriculados por curso
def students_by_course_view(request):
    students_by_course = Enrollment.objects.values(
        'course__course_name', 'course__course_code'
    ).annotate(total_students=Count('student')).order_by('-total_students')

    context = {
        'students_by_course': students_by_course,
    }
    return render(request, 'enrollments/students_by_course.html', context)

# Reporte: Profesores con más estudiantes
def teachers_with_most_students_view(request):
    from courses.models import Course
    from teachers.models import Teacher

    teachers = Teacher.objects.annotate(
        total_students=Count('courses__enrollments')
    ).order_by('-total_students')

    context = {
        'teachers': teachers,
    }
    return render(request, 'enrollments/teachers_with_most_students.html', context)
