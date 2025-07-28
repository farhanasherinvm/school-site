from django.urls import path, include
from .views import JobApplicationViewSet, JobOpeningViewSet, JobSeekerCreateView,EmployerCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobs', JobOpeningViewSet, basename='job')
router.register(r'applications', JobApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
    path('jobseekers/register/', JobSeekerCreateView.as_view(), name='jobseeker-register'),
    path('employers/register/', EmployerCreateView.as_view(), name='employer-register'),


]
