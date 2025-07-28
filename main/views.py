from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import JobOpening, JobApplication
from .serializers import JobOpeningSerializer, JobApplicationSerializer, JobSeekerSerializer, EmployerSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import JobSeekerSerializer
from .models import CustomUser




class JobSeekerCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = JobSeekerSerializer

class EmployerCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = EmployerSerializer    


# JOB OPENINGS
class JobOpeningViewSet(viewsets.ModelViewSet):
    serializer_class = JobOpeningSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        return JobOpening.objects.filter(is_deleted=False).order_by('-created_at')

    def perform_create(self, serializer):
        # Only employers or admins can create jobs
        if self.request.user.role not in ['employer', 'admin']:
            raise PermissionError("Only employers or admins can post job openings.")
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        # Only the employer who created the job or an admin can update it
        job = self.get_object()
        if self.request.user != job.created_by and self.request.user.role != 'admin':
            raise PermissionError("You don't have permission to update this job.")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        # Soft delete: Only job creator or admin can delete
        job = self.get_object()
        if request.user != job.created_by and request.user.role != 'admin':
            return Response({"error": "You don't have permission to delete this job."}, status=status.HTTP_403_FORBIDDEN)
        job.is_deleted = True
        job.save()
        return Response({"message": "Job opening deleted successfully."}, status=status.HTTP_200_OK)


# JOB APPLICATIONS
class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_queryset(self):
        user = self.request.user
        # Jobseekers see their own applications, employers/admins see all
        if user.role in ['employer', 'admin']:
            return JobApplication.objects.filter(is_deleted=False)
        return JobApplication.objects.filter(applicant=user, is_deleted=False)

    def perform_create(self, serializer):
        # Only jobseekers can apply
        if self.request.user.role != 'jobseeker':
            raise PermissionError("Only jobseekers can apply for jobs.")
        serializer.save(applicant=self.request.user)

    def destroy(self, request, *args, **kwargs):
        application = self.get_object()
        # Jobseekers can delete only their applications; admins can delete any
        if request.user != application.applicant and request.user.role != 'admin':
            return Response({"error": "You don't have permission to delete this application."}, status=status.HTTP_403_FORBIDDEN)
        application.is_deleted = True
        application.save()
        return Response({"message": "Job application deleted successfully."}, status=status.HTTP_200_OK)