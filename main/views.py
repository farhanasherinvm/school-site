from rest_framework import viewsets, permissions,status
from .models import Job, JobApplication
from .serializers import UserSerializer, JobSerializer, ApplicationSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response




User = get_user_model()

# Signup
from rest_framework.generics import CreateAPIView
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Jobs
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

# Apply
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
      serializer.save(applicant=self.request.user)

     #delete = soft delete
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({ "Application deleted "}, status=status.HTTP_204_NO_CONTENT)

    #  Only allow update by owner (applicant)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.applicant != request.user:
            return Response({ "Not allowed to update this application."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)