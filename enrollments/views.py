from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count
from .models import Enrollment
from .forms import EnrollmentForm, EnrollmentUpdateForm

class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollments/enrollment_list.html'
    context_object_name = 'enrollments'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments_by_course'] = Enrollment.objects.values(
            'course__course_name'
        ).annotate(
            total=Count('id')
        )
        return context

class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    form_class = EnrollmentUpdateForm
    template_name = 'enrollments/enrollment_form.html'
    success_url = reverse_lazy('enrollment-list')

class EnrollmentDeleteView(DeleteView):
    model = Enrollment
    template_name = 'enrollments/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment-list')