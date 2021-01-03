from django.shortcuts import render
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
# Create your views here.

class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseAPI(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseCreateAPI(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class CourseUpdateAPI(UpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
 