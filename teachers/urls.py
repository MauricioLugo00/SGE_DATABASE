from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeacherListView.as_view(), name='teacher-list'),
    path('create/', views.TeacherCreateView.as_view(), name='teacher-create'),
    path('<int:pk>/update/', views.TeacherUpdateView.as_view(), name='teacher-update'),
    path('<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher-delete'),
    path('statistics/', views.teacher_statistics_view, name='teacher-statistics'),
]
