from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Course
from .forms import CourseForm

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    ordering = ['course_code']

# Crear curso
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

# Actualizar curso
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course-list')

# Eliminar curso
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course-list')

# Vista para estadísticas del curso
def course_statistics_view(request):
    courses_with_enrollment = Course.objects.annotate(total_students=Count('enrollments'))

    context = {
        'courses_with_enrollment': courses_with_enrollment,
    }
    return render(request, 'courses/course_statistics.html', context)
