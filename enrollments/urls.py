from django.urls import path
from . import views

urlpatterns = [
    path('', views.EnrollmentListView.as_view(), name='enrollment-list'),
    path('create/', views.EnrollmentCreateView.as_view(), name='enrollment-create'),
    path('<int:pk>/update/', views.EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('<int:pk>/delete/', views.EnrollmentDeleteView.as_view(), name='enrollment-delete'),
]