from rest_framework import generics, permissions
from .models import Teacher
from .serializers import TeacherSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import filters

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'subject']
    ordering_fields = ['first_name', 'last_name', 'joining_date']

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]