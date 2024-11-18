from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Teacher
from .forms import TeacherForm
from django.shortcuts import render

# Vista para listar todos los profesores
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    context_object_name = 'teachers'
    ordering = ['last_name', 'first_name']

# Vista para crear un nuevo profesor
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

# Vista para actualizar un profesor
class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teachers/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

# Vista para eliminar un profesor
class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher-list')

# Vista para consultas avanzadas
def teacher_statistics_view(request):
    # Profesores con especializaciones únicas
    teachers_by_specialization = Teacher.objects.values('specialization').annotate(total=Count('id'))

    context = {
        'teachers_by_specialization': teachers_by_specialization,
    }
    return render(request, 'teachers/teacher_statistics.html', context)
