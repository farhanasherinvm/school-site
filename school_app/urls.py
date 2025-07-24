from django.urls import path
from .views import (
    TeacherListCreateView,
    TeacherDetailView,
    StudentListCreateView,
    StudentDetailView
)

urlpatterns = [
    # Teacher endpoints
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),

    # Student endpoints
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
]
