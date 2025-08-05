from rest_framework import serializers
from .models import CustomUser, Job, JobApplication
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'full_name', 'role', 'password')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.ReadOnlyField(source='employer.email')

    class Meta:
        model = Job
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    jobseeker = serializers.ReadOnlyField(source='jobseeker.email')

    class Meta:
        model = JobApplication
        fields = '__all__'
        read_only_fields = ['applicant', 'status', 'applied_on', 'is_deleted']
