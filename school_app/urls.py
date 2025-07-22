from django.urls import path
from .views import TeacherListCreateView, TeacherDetailView

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]