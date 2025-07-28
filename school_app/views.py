from rest_framework import generics, permissions
from .models import Teacher,Advertisement
from .serializers import TeacherSerializer,AdvertisementSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


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


class AdvertisementListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request):
        ads = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ads, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdvertisementDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Advertisement, pk=pk)

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdvertisementSerializer(ad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ad = self.get_object(pk)
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)