from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['department', 'status']  # Filter by these fields
    search_fields = ['name']  # Search by student name