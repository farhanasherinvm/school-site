from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('joining_date',)
        
    def validate_email(self, value):
        if Teacher.objects.filter(email=value).exists():
            raise serializers.ValidationError("A teacher with this email already exists.")
        return value