from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Avg
from .models import Student
from .forms import StudentForm

# Vista para listar todos los estudiantes
class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    ordering = ['last_name', 'first_name']

# Vista para crear un nuevo estudiante
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

# Vista para actualizar un estudiante
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student-list')

# Vista para eliminar un estudiante
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student-list')

# Vista para consultas avanzadas
def student_statistics_view(request):
    # Total de estudiantes
    total_students = Student.objects.count()
    # Promedio de edad de los estudiantes
    avg_age = Student.objects.aggregate(Avg('date_of_birth'))

    context = {
        'total_students': total_students,
        'avg_age': avg_age.get('date_of_birth__avg')
    }
    return render(request, 'students/student_statistics.html', context)
