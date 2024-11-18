from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnrollmentListView.as_view(), name='enrollment-list'),
    path('create/', views.EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('<int:pk>/update/', views.EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('<int:pk>/delete/', views.EnrollmentDeleteView.as_view(), name='enrollment-delete'),
    path('students-by-course/', views.students_by_course_view, name='students-by-course'),
    path('teachers-with-most-students/', views.teachers_with_most_students_view, name='teachers-with-most-students'),
]
