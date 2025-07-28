from django.urls import path
from .views import TeacherListCreateView, TeacherDetailView,AdvertisementListCreateAPIView,AdvertisementDetailAPIView

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('ads/', AdvertisementListCreateAPIView.as_view(), name='ad-list-create'),
    path('ads/<int:pk>/', AdvertisementDetailAPIView.as_view(), name='ad-detail'),
]