from django.shortcuts import render
from rest_framework import viewsets
from .models import Student,Employer,Post,Application
from .serializers import StudentSerializer,EmployerSerializer,PostSerializer,ApplicationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class EmployerViewSet(viewsets.ModelViewSet):
    queryset=Employer.objects.all()
    serializer_class=EmployerSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset=Application.objects.all()
    serializer_class=ApplicationSerializer