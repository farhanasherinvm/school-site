from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Teacher, Student  # import both models

admin.site.register(Teacher)
admin.site.register(Student)
